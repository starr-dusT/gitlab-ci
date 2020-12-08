#!/usr/bin/env python3

# Standard libraries
from tempfile import NamedTemporaryFile

# Files class
class Files:

    # Temp
    @staticmethod
    def temp(path=None, mode='wt', newline='\n', prefix='.tmp.'):

        # Create temporary file
        temp_file = NamedTemporaryFile(delete=False, dir=path, mode=mode, newline=newline,
                                       prefix=prefix)

        # Result
        return temp_file
