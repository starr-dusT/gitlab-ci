#!/usr/bin/env python3

# Standard libraries
from os import sep
from pathlib import PurePosixPath
from sys import platform, stdin, stdout

# Platform
class Platform:

    # Constants
    IS_LINUX = (platform in ['linux', 'linux2'])
    IS_WINDOWS = (platform in ['win32'])

    # Paths
    BUILDS_DIR = PurePosixPath('/builds')

    # Separators
    PATH_SEPARATOR = sep

    # TTYs
    IS_TTY_STDIN = stdin.isatty() and stdin.encoding != 'cp1252'
    IS_TTY_STDOUT = stdout.isatty()
