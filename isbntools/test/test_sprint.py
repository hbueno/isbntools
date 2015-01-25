#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

import os
import sys

from nose.tools import assert_equals
from isbnlib.dev.bouth23 import u, b

from isbntools._lab import sprint
from isbntools.test.adapters import run_code

"""
nose tests
"""

WINDOWS = os.name == 'nt'


# def test_sprint1():
#    try:
#        sprint('海明威')
#    except:
#        raise

def test_sprint():
    code = "from isbnlib.dev.bouth23 import u;from isbntools._lab import sprint;sprint(u('abc'))"
    if WINDOWS:
        assert_equals(run_code(code), b('abc\r\n'))
    else:
        assert_equals(run_code(code), b('abc\n'))
