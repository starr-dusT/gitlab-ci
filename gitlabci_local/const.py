#!/usr/bin/env python3

# Libraries
from os import sep
from pathlib import PurePosixPath
from sys import platform

# Platform
class Platform:

    # Constants
    IS_LINUX = (platform == 'linux' or platform == 'linux2')
    IS_WINDOWS = (platform == 'win32')

    # Paths
    BUILDS_DIR = PurePosixPath('/builds')

    # Separators
    PATH_SEPARATOR = sep
