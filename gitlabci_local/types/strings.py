#!/usr/bin/env python3

# Components
from ..prints.colors import Colors

# Strings class
class Strings:

    # Center
    @staticmethod
    def center(string, length):

        # Extract text
        text = Strings.strip(string)

        # Center string
        if len(text) < length:
            paddings = length - len(text)
            left = paddings // 2
            right = -(-paddings // 2)
            return ' ' * left + string + ' ' * right

        # Default string
        return string

    # Strip
    @staticmethod
    def strip(string):
        for item in Colors.ALL:
            string = string.replace(item, '')
        return string
