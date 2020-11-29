#!/usr/bin/env python3

# Volumes class
class Volumes:

    # Members
    _volumes = None

    # Constructor
    def __init__(self):
        self._volumes = dict()

    # Add
    def add(self, source, target, mode, override):

        # Handle overrides
        if target in [self._volumes[volume]['bind'] for volume in self._volumes]:
            if override:
                return
            else:
                duplicates = [
                    volume for volume in self._volumes
                    if volume.endswith(source) and self._volumes[volume]['bind'] == target
                ]
                if duplicates:
                    self._volumes.pop(duplicates[0])

        # Adapt source to allow duplicates
        while source in self._volumes:
            source = '/.' + source

        # Add volume binding
        self._volumes[source] = { #
            'bind': target,
            'mode': mode
        }

    # Get
    def get(self):
        return self._volumes
