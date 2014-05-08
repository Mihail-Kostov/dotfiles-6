#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
optimize_path
"""
from collections import OrderedDict, Counter
import json
import logging
import os
import re
import subprocess

log = logging.getLogger()

CHECKSUM_BIN='md5sum'

def sbin_policy(iterable):
    """
    # TODO: static optimizations
    """
    for s in sorted(
        (
            (
                (int('/sbin' not in x)*2) +
                (int('/usr/local' in x)*3) +
                (int('/home' in x)*4)
            ),
            len(x),
            x)
            for x in iterable ):
        #logging.debug(s)
        yield s[-1]


def optimize_path(iterable, strip=None, sortfunc=sbin_policy):
    """
    optimize paths
    """
    if strip:
        pattern = re.compile( strip )
        log.debug((pattern, strip, ))
        keys = (p.strip() for p in iterable if not pattern.match(p))
    else:
        keys = (p.strip() for p in iterable)

    paths = OrderedDict.fromkeys(keys)

    if sortfunc:
        return sortfunc(paths.iterkeys())
    else:
        return paths.iterkeys()


def get_checksum(path, hashbin=CHECKSUM_BIN):
    logging.debug((hashbin,path))
    if os.path.isfile(path):
        if os.access(path, os.R_OK):
            return (subprocess.check_output( (hashbin, path) ).rstrip() +
                    (os.path.islink(path) and " -> %s" % os.path.realpath(path) or '') )
    return ('?  %s' % path)


def detect_duplicates(iterable):
    paths = OrderedDict()
    for path in iterable:
        for f in os.listdir(path):
            basename = os.path.basename(f)
            basename_paths = paths.get(basename,[])
            basename_paths.append(path)
            paths[basename] = basename_paths


    annotated_paths = (
        (k, [get_checksum( os.path.join(p,k) ) for p in v] )
            for (k,v) in paths.iteritems() if len(v) > 1)

    def label(v):
        counts = Counter(l.split()[0] for l in v)
        #logging.debug(counts)
        if len(v) in counts.itervalues():
            return {'type':'duplicates', 'files': sorted(v)}
        else:
            return {'type':'hashes', 'files': v}

    return OrderedDict(
        (k, label(v)) for (k,v) in annotated_paths
    )


def check_difference(iterable):
    raise NotImplementedError()
    import difflib

    iterable = list(iterable)
    regular = list( optimize_path( iterable, sortfunc=None) )
    optimized = list( optimize_path( iterable, sortfunc=sbin_policy ) )

    logging.debug(regular)
    logging.debug(optimized)

    return '\n'.join( difflib.ndiff(regular, optimized) )
    # detect colli

import unittest
import sys
from StringIO import StringIO

class ShellTestCase(unittest.TestCase):
    __stdout = sys.stdout
    __stderr = sys.stderr
    def _run_command(self, _cmd):
        # TODO: not monkey-patch sys.stderr
        try:
            #process = subprocess.Popen((here,) + cmd,
            #    stdout=subprocess.PIPE,
            #    stderr=subprocess.PIPE)
            #stdout,stderr = process.communicate()
            #logging.debug(_cmd)
            logging.info("### TEST CASE: %r" % _cmd)

            stdout = sys.stdout = StringIO()
            stderr = sys.stderr = StringIO()

            sys.argv = _cmd
            main()

            _stderr = stderr.read()
            _stdout = stdout.read() # ..
        finally:
            sys.stdout = self.__stdout
            sys.stderr = self.__stderr

            logging.debug('# >2\n%s',_stderr)
            logging.debug('# >1\n%s', _stdout)
            return _stderr, _stdout

class Test_optimize_path(ShellTestCase):
    def test_optimize_path(self):
        print( '\n'.join( optimize_path(os.environ['PATH'].split(':')) ) )

    def test_script(self):
        cmds = (
         ('-p', ),
         ('-c', ),
         #('-w','hashes', ),
         #('-w','duplicates', ),
        )
        here = os.path.abspath(__file__)

        for cmd in cmds:
            _cmd = [here, ] + list(cmd)
            stderr, stdout = self._run_command(_cmd)
            self.assertEqual(len(stderr), 0)








def main(*_args):
    import optparse
    import logging
    import sys

    prs = optparse.OptionParser(usage="./%prog : args")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    prs.add_option('-p', '--print',
                    dest='print',
                    action='store_true',)
    prs.add_option('-d', '--delim',
                    dest='delim',
                    action='store',
                    default='\n')
    prs.add_option('-s', '--strip',
                    dest='strip',
                    action='store',
                    help='Regex expression to strip from path')

    prs.add_option('-c', '--check',
                    dest='check',
                    action='store_true',
                    help='Detect lookup variance on path')
    prs.add_option('-w', '--whichpackage',
                    dest='pkg_lookup',
                    action='store',
                    default=None,
                    help='Run `wajig whichpackage $path`')

    (opts, args) = prs.parse_args(_args or sys.argv[1:])

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())

    iterable = os.environ['PATH'].split(':')

    iterable = list( optimize_path(iterable, opts.strip) )
    if opts.verbose:
        iterable, output = tee(iterable)
        for i in output:
            logging.info(i)

    if opts.print:
        print( opts.delim.join( iterable ) )

    duplicates = tuple()
    if opts.check:
        duplicates = detect_duplicates(iterable)
        print(json.dumps(duplicates, indent=3))

    if opts.pkg_lookup:
        duplicates = duplicates or detect_duplicates(iterable)

        # emit,yield,return
        from collections import namedtuple
        File = namedtuple('File', ('path','package', 'hash'))
        File.__str__ = lambda self: ("%-20s\t%s\t%s" %
                        (   self.package or '?',
                            self.path,
                            not self.package and self.hash or ''))

        for (k,v) in duplicates.iteritems():
            if v.get('type', None) == opts.pkg_lookup:
                for path in v.get('files'):
                    hash, path = path.split()
                    package = subprocess.check_output(
                            ('wajig','whichpackage', path)
                        ).split(':')[0].strip()
                    _file = File(path, package, hash)
                    logging.info(str(_file))


if __name__ == "__main__":
    main()
