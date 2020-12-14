#!/usr/bin/env python3

# Standard libraries
from os import environ

# Modules libraries
from pexpect_executor import Executor

# Engine
environ['CI_LOCAL_ENGINE'] = 'docker,auto'

# Configure
Executor.configure(host='preview', tool='gitlabci-local')

# Jobs selector
Executor('gitlabci-local', workdir='./examples/').\
    read().\
    press(Executor.KEY_SPACE).\
    read().\
    press(Executor.KEY_DOWN).\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_SPACE).\
    read().\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_SPACE).\
    read().\
    press(Executor.KEY_DOWN).\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_SPACE).\
    read().\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_SPACE).\
    read().\
    wait(2).\
    press(Executor.KEY_ENTER).\
    finish()

# Job selector
Executor('gitlabci-local -l').\
    read().\
    press(Executor.KEY_SPACE).\
    read().\
    press(Executor.KEY_DOWN).\
    press(Executor.KEY_DOWN).\
    press(Executor.KEY_DOWN).\
    press(Executor.KEY_DOWN).\
    read().\
    wait(2).\
    press(Executor.KEY_ENTER).\
    finish()

# Job runner
Executor('gitlabci-local \'Job 1 - 3\'').\
    finish()

# Pipeline runner
Executor('gitlabci-local -p', workdir='../tests/failures/').\
    finish()

# Stage runner
Executor('gitlabci-local -p one two', workdir='../stages/').\
    finish()

# Configurations runner
Executor('gitlabci-local -e VARIABLE_8=\'value8\' -e VARIABLE_11=value11 -p', workdir='../configurations/').\
    read().\
    wait(1).\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    press('input').\
    read().\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    read().\
    press('_default').\
    read().\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    press(Executor.KEY_DOWN).\
    read().\
    wait(1).\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    press(Executor.KEY_DOWN).\
    read().\
    wait(1).\
    press(Executor.KEY_ENTER).\
    read().\
    wait(1).\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_DOWN).\
    read().\
    press(Executor.KEY_ENTER).\
    read().\
    press(Executor.KEY_ENTER).\
    read().\
    finish()

# Prompt
Executor('').\
    finish()
