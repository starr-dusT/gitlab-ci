#!/usr/bin/env python3
import getpass
import os
import pexpect
import sys
import time

# Constants
KEY_UP = '\033[A'
KEY_DOWN = '\033[B'
KEY_ENTER = '\r'
KEY_SPACE = ' '

# Executor
class executor:
    child = None

    # Constructor
    def __init__(self, command, workdir=None):
        if workdir:
            self.prompt('cd %s' % workdir)
            os.chdir(workdir)
        self.prompt(command)
        if command:
            self.child = pexpect.spawn(command)

    # Prompter
    def prompt(self, command):
        print('\033[32m%s@preview \033[33mgitlabci-local\033[0m $ ' % (getpass.getuser()),
              end='', flush=True)
        time.sleep(1)
        if command:
            print('%s ' % (command), end='', flush=True)
        else:
            time.sleep(10)
            print('', flush=True)
        time.sleep(2)
        print(' ', flush=True)

    # Interactor
    def interact(self, key):
        self.child.send(key)
        return self

    # Reader
    def read(self):
        while True:
            try:
                output = self.child.read_nonblocking(size=1024, timeout=1)
            except:
                output = None
            if not output:
                break
            output = output.decode('utf-8', errors='ignore')
            output = output.replace('\x1b[6n', '')
            print(output, end='', flush=True)
        return self

    # Waiter
    def wait(self, delay):
        time.sleep(delay)
        return self

    # Finished
    def finish(self):
        self.read()
        time.sleep(1)
        return self

# Header
for i in range(1, 30):
    print(' ', flush=True)

# Delay
time.sleep(3)

# Help
executor('gitlabci-local -h').\
    read().\
    finish()

# Jobs selector
executor('gitlabci-local', './examples/').\
    read().\
    interact(KEY_SPACE).\
    read().\
    interact(KEY_DOWN).\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_SPACE).\
    read().\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_SPACE).\
    read().\
    interact(KEY_DOWN).\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_SPACE).\
    read().\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_SPACE).\
    read().\
    wait(2).\
    interact(KEY_ENTER).\
    finish()

# Job selector
executor('gitlabci-local -l').\
    read().\
    interact(KEY_SPACE).\
    read().\
    interact(KEY_DOWN).\
    interact(KEY_DOWN).\
    interact(KEY_DOWN).\
    interact(KEY_DOWN).\
    read().\
    wait(2).\
    interact(KEY_ENTER).\
    finish()

# Job runner
executor('gitlabci-local -b -a "Job 1 - 3"').\
    finish()

# Pipeline runner
executor('gitlabci-local -b -a -p', '../tests/failures/').\
    finish()

# Stage runner
executor('gitlabci-local -p one two', '../stages/').\
    finish()

# Configurations runner
executor('gitlabci-local -e VARIABLE_8="value8" -e VARIABLE_11=value11 -p', '../configurations/').\
    read().\
    wait(1).\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    interact('input').\
    read().\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    read().\
    interact('_default').\
    read().\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    interact(KEY_DOWN).\
    read().\
    wait(1).\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    interact(KEY_DOWN).\
    read().\
    wait(1).\
    interact(KEY_ENTER).\
    read().\
    wait(1).\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_DOWN).\
    read().\
    interact(KEY_ENTER).\
    read().\
    finish()

# Prompt
executor('').\
    finish()

# Delay
time.sleep(10)
