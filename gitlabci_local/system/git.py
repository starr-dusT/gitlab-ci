#!/usr/bin/env python3

# Standard libraries
from subprocess import CalledProcessError, check_output, DEVNULL

# Git class
class Git:

    # Constants
    __BINARY = 'git'

    # HEAD revision hash
    @staticmethod
    def head_revision_hash(workdir=None):

        # Result
        try:
            return check_output(
                [Git.__BINARY, 'rev-parse', 'HEAD'],
                cwd=workdir,
                shell=False,
                stderr=DEVNULL,
            ).strip().decode()
        except CalledProcessError:
            return ''

    # HEAD revision short hash
    @staticmethod
    def head_revision_short_hash(workdir=None):

        # Result
        try:
            return check_output(
                [Git.__BINARY, 'rev-parse', '--short', 'HEAD'],
                cwd=workdir,
                shell=False,
                stderr=DEVNULL,
            ).strip().decode()
        except CalledProcessError:
            return ''
