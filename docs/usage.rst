Usage
=======
List commands::

    python setup.py --help
    python setup.py --help-commands
    python setup.py test --help
    # bash scripts/bootstrap_dotfiles.sh -h
    # less_ Makefile
    # make help
    # make <tab>
    # make vim_help
    # vim: :ListMappings

Install dev, docs. testing, and suggests from pip requirements files::

    pip install -r ./requirements-all.txt
    # make pip_install_requirements_all


bootstrap_dotfiles.sh
-----------------------

``bash scripts/bootstrap_dotfiles.sh``:

.. program-output:: bash ../scripts/bootstrap_dotfiles.sh -h


dotfiles Makefile
-------------------
``make help``:

.. program-output:: cd .. && make help
   :shell:


Bash
-----
``make help_bash_rst``:

.. include:: bash_conf.rst   


Vim
-----
``make help_vim_rst``:

.. include:: dotvim_conf.rst


I3wm
-----
``make help_i3_rst``:

.. include:: i3_conf.rst



Scripts
---------
In ``scripts/``

**bashmarks_to_nerdtree.sh**
   Convert `bashmarks` shortcut variables
   starting with ``DIR_`` to `NERDTreeBookmarks <NERDTree>`_ format::

       l
       ./bashmarks_to_nerdtree.sh | tee ~/.NERDTreeBookmarks

**bootstrap_dotfiles.sh**
   Clone, update, and install dotfiles in ``$HOME``

    See: `bootstrap_dotfiles.sh`_

**compare_installed.py**
   Compare packages listed in a debian/ubuntu APT
   ``.manifest`` with installed packages.

   See: https://github.com/westurner/pkgsetcomp

**gittagstohgtags.sh**
   Convert ``git`` tags to ``hgtags`` format

**pulse.sh**
   Setup, configure, start, stop, and restart ``pulseaudio``

**setup_mathjax.py**
   Setup ``MathJax``

**setup_pandas_notebook_deb.sh**
   Setup ``IPython Notebook``, ``Scipy``, ``Numpy``, ``Pandas``
   with Ubuntu packages and pip

**setup_pandas_notebook.sh**
   Setup ``Brew``, ``IPython Notebook``, ``scipy``, ``numpy``,
   and pandas on OSX

**setup_scipy_deb.py**
   Install and symlink ``scipy``, ``numpy``, and ``matplotlib`` from ``apt``


**deb_deps.py**
   Work with debian dependencies

**deb_search.py**
   Search for a debian package

**build_docs.py**
   Build sets of sphinx documentation projects

**greppaths.py**
   Grep

**lsof.py**
   lsof subprocess wrapper

**mactool.py**
   MAC address tool

**optimizepath.py**
   Work with PATH as an ordered set

**passwordstrength.py**
   Gauge password strength

**pipls.py**
   Walk and enumerate a pip requirements file

**pycut.py**
   Similar to ``coreutils``' ``cut``: split line-based files into fields

**py_index.py**
   Create a python package index HTML file for a directory of
   packages. (``.egg``, ``.zip``, ``.tar.gz``, ``tgz``)

**pyline.py**
   Similar to ``sed`` and ``awk``:
   Execute python expressions over line-based files.

   See: https://github.com/westurner/pyline

**pyren.py**
   Skeleton regex file rename script

**repos.py**
   Wrap version control system commandline interfaces

   See: https://github.com/westurner/pyrpo

**usrlog.py**
   Search through ``.usrlog`` files
