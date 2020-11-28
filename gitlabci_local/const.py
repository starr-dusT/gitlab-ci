#!/usr/bin/env python3

# Libraries
from pathlib import PurePosixPath
from sys import platform

# Platform
class Platform:

    # Constants
    IS_LINUX = (platform == 'linux' or platform == 'linux2')
    IS_WINDOWS = (platform == 'win32')

    # Paths
    BUILDS_DIR = PurePosixPath('/builds')
    TEMP_DIR = PurePosixPath('/tmp')
    TEMP_ENTRYPOINTS_DIR = PurePosixPath('/tmp/gitlabci-local')
