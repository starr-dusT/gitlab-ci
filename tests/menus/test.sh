#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
pexpect-executor --space --enter gitlabci-local
pexpect-executor --press a --enter gitlabci-local
pexpect-executor --press a --enter -- gitlabci-local -s 'Job 1'
pexpect-executor --down --down --space --enter -- gitlabci-local -m
pexpect-executor --space --enter -- gitlabci-local -p -s
pexpect-executor --space --enter -- gitlabci-local -p -s menus-1
pexpect-executor -- gitlabci-local -p -s menus-0
pexpect-executor --up --up --space --enter -- gitlabci-local -p -m -l
pexpect-executor --ctrl c -- gitlabci-local -p -m -l
pexpect-executor --space --enter -- gitlabci-local -c ./.gitlab-ci.select.yml -s
pexpect-executor --enter -- gitlabci-local -c ./.gitlab-ci.select.yml -l
