#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
pyfindmodule -- find the path to a python module (.py, .pyc, .pyo)
"""

from collections import OrderedDict
from importlib import import_module
import os
import sys

import logging
log = logging.getLogger()


class ModuleNotFoundError(ImportError):
    pass


def pyfindmodule(searchstr):
    """mainfunc

    Arguments:
         (str): ...

    Keyword Arguments:
         (str): ...

    Returns:
        str: ...

    Yields:
        str: ...

    Raises:
        Exception: ...
    """
    if '*' in searchstr:
        raise ValueError(searchstr)
    try:
        module = import_module(searchstr)
    except ImportError as e:
        raise ModuleNotFoundError(e)
    cfg = OrderedDict()
    cfg['path'] = module_path = module.__file__
    if module_path.endswith('.pyc'):
        _module_srcpath = u"%s.py" % module_path[:-4]
        if os.path.exists(_module_srcpath):
            log.info(('module.srcpath', _module_srcpath,))
            cfg['srcpath'] = _module_srcpath
    return cfg
    #return pkg_resources.resource_filename(searchstr, '')



import sys
import unittest


class Test_pyfindmodule(unittest.TestCase):

    def setUp(self):
        pass

    def test_pyfindmodule(self):
        io = [
            [('string'), None],
            [('collections'), None]
        ]
        io.extend(((x, None) for x in sys.builtin_module_names))
        for I, O in io:
            output = pyfindmodule(I)
            assert (I, output) == (I, O)
        pass

    def tearDown(self):
        pass


def main(argv=None):
    """
    Main function

    Keyword Arguments:
        argv (list): commandline arguments (e.g. sys.argv[1:])
    Returns:
        int:
    """
    import logging
    import optparse

    prs = optparse.OptionParser(usage="%prog : args")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)


    (opts, args) = prs.parse_args(args=argv)
    loglevel = logging.INFO
    if opts.verbose:
        loglevel = logging.DEBUG
    elif opts.quiet:
        loglevel = logging.ERROR
    logging.basicConfig(level=loglevel)
    log = logging.getLogger()
    argv = list(argv) if argv else []
    log.debug('argv: %r', argv)
    log.debug('opts: %r', opts)
    log.debug('args: %r', args)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        return unittest.main()

    EX_OK = 0
    for arg in args:
        output = pyfindmodule(arg)
        print(arg)
        print(output)
    return EX_OK


if __name__ == "__main__":
    import sys
    sys.exit(main(argv=sys.argv[1:]))