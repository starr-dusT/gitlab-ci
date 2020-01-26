#!/usr/bin/env python3

# Libraries
import getpass
import os
import pexpect
import sys
import time

# Executor
class Executor:

    # Constants
    KEY_UP = '\033[A'
    KEY_DOWN = '\033[B'
    KEY_ENTER = '\r'
    KEY_SPACE = ' '

    # Variables
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
Executor('gitlabci-local -h').\
    read().\
    finish()

# Jobs selector
Executor('gitlabci-local', './examples/').\
    read().\
    interact(Executor.KEY_SPACE).\
    read().\
    interact(Executor.KEY_DOWN).\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_SPACE).\
    read().\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_SPACE).\
    read().\
    interact(Executor.KEY_DOWN).\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_SPACE).\
    read().\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_SPACE).\
    read().\
    wait(2).\
    interact(Executor.KEY_ENTER).\
    finish()

# Job selector
Executor('gitlabci-local -l').\
    read().\
    interact(Executor.KEY_SPACE).\
    read().\
    interact(Executor.KEY_DOWN).\
    interact(Executor.KEY_DOWN).\
    interact(Executor.KEY_DOWN).\
    interact(Executor.KEY_DOWN).\
    read().\
    wait(2).\
    interact(Executor.KEY_ENTER).\
    finish()

# Job runner
Executor('gitlabci-local -b -a "Job 1 - 3"').\
    finish()

# Pipeline runner
Executor('gitlabci-local -b -a -p', '../tests/failures/').\
    finish()

# Stage runner
Executor('gitlabci-local -p one two', '../stages/').\
    finish()

# Configurations runner
Executor('gitlabci-local -e VARIABLE_8="value8" -e VARIABLE_11=value11 -p', '../configurations/').\
    read().\
    wait(1).\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    interact('input').\
    read().\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    read().\
    interact('_default').\
    read().\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    interact(Executor.KEY_DOWN).\
    read().\
    wait(1).\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    interact(Executor.KEY_DOWN).\
    read().\
    wait(1).\
    interact(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_DOWN).\
    read().\
    interact(Executor.KEY_ENTER).\
    read().\
    finish()

# Prompt
Executor('').\
    finish()

# Delay
time.sleep(10)
