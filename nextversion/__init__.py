# -*- coding: utf-8 -*-
"""
    nextversion
    ~~~~~~~~~~~

    Increments module verision numbers.::

        from nextversion import nextversion
        nextversion('1.0rc2')   # => '1.0rc3'
        nextversion('v1.0rc2')  # => '1.0rc3'  (normalized to compatible version with PEP 386)
        nextversion('foo.0.3')  # => None      (impossible to normalize)

    If original version number does not match `PEP 386 <//www.python.org/dev/peps/pep-0386/>`_ ,

    1. Next version compatible with `PEP 386 <//www.python.org/dev/peps/pep-0386/>`_ is returned if possible,
    2. If impossible, `None` is returned.
"""
__version__   = '0.1.0'
__author__    = 'Sho Nakatani'
__email__     = 'lay.sakura@gmail.com'
__copyright__ = 'Copyright 2013, Sho Nakatani'


def nextversion(current_version):
    return '1.0'
