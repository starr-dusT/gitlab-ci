#!/usr/bin/env python3

# Libraries
from sys import platform

# Platform
class Platform:

    # Constants
    IS_LINUX = (platform == 'linux' or platform == 'linux2')
    IS_WINDOWS = (platform == 'win32')

    # Paths
    BUILDS_DIR = '/builds'
    TEMP_DIR = '/tmp'
