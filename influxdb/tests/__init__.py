# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
    using_py26 = "py26"
    skipIfPy26 = unittest.skipIf(using_py26, "Skipping this test on py26")
else:
    import unittest
using_pypy = hasattr(sys, "pypy_version_info")
skipIfPYpy = unittest.skipIf(using_pypy, "Skipping this test on pypy.")

_skip_server_tests = os.environ.get(
    'INFLUXDB_PYTHON_SKIP_SERVER_TESTS',
    None) == 'True'
skipServerTests = unittest.skipIf(_skip_server_tests,
                                  "Skipping server tests...")
