#!/usr/bin/env python3

# Standard libraries
from os import environ
from time import localtime, strftime, time
from update_checker import pretty_date, UpdateChecker

# Components
from ..prints.colors import Colors
from ..system.platform import Platform
from .version import Version

# Updates class
class Updates:

    # Members
    __enabled = False
    __name = None
    __settings = None
    __version = None

    # Constructor
    def __init__(self, name, settings):

        # Initialize members
        self.__name = name
        self.__settings = settings
        self.__version = Version.get()

        # Acquire enabled
        enabled = self.__settings.get('updates', 'enabled')
        if not enabled:
            enabled = 1
            self.__settings.set('updates', 'enabled', enabled)

        # Check enabled
        self.__enabled = int(enabled) == 1 and 'CI_LOCAL_UPDATES_DISABLE' not in environ

    # Checker
    def check(self, older=False):

        # Check for updates
        check = UpdateChecker(bypass_cache=True).check(
            self.__name, '0.0.0' if older else self.__version)
        if check:

            # Show newer updates
            print(' ')
            print(' %sINFO: %s%s %s was released%s %s(current version is %s)%s' %
                  (Colors.YELLOW, Colors.GREEN, self.__name, check.available_version,
                   ' ' + pretty_date(check.release_date) if check.release_date else '',
                   Colors.BOLD, self.__version, Colors.RESET))
            print(' ')
            Platform.flush()
            return True

        # Older offline failure
        if older:

            # Show current updates
            print(' ')
            print(
                ' %sWARNING: %s%s was not found, network might be down %s(current version is %s)%s'
                % (Colors.YELLOW, Colors.RED, self.__name, Colors.BOLD, self.__version,
                   Colors.RESET))
            print(' ')
            Platform.flush()
            return True

        # Result
        return False

    # Daily
    def daily(self):

        # Acquire updates check last timestamp
        last = self.__settings.get('updates', 'last_timestamp')

        # Handle daily checks
        current = int(time())
        if not last or strftime('%Y-%m-%d', localtime(current)) != strftime(
                '%Y-%m-%d', localtime(int(last))):
            self.__settings.set('updates', 'last_timestamp', current)
            return True

        # Default fallback
        return False

    # Enabled
    def enabled(self):
        return self.__enabled
