# Copyright (c) 2024 Jan T. Müller <mail@jantmueller.com>

import sys

from setuptools import setup

if sys.version_info < (3, 8):
    sys.exit("ERROR: totify requires Python 3.8+")

setup()
