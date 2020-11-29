#!/usr/bin/env python3

# Volumes class
class Volumes:

    # Members
    _volumes = None

    # Constructor
    def __init__(self):
        self._volumes = dict()

    # Add
    def add(self, source, target, mode):
        while source in self._volumes:
            source = '/.' + source
        self._volumes[source] = { #
            'bind': target,
            'mode': mode
        }

    # Get
    def get(self):
        return self._volumes
