#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local -p </dev/null && exit 1 || true
VARIABLE_8=value8 gitlabci-local -p </dev/null && exit 1 || true
VARIABLE_8= VARIABLE_12=value12 gitlabci-local -p </dev/null
gitlabci-local -e VARIABLE_8=value8 -e VARIABLE_12=value12 -p </dev/null
gitlabci-local -e VARIABLE_8=value8 -e VARIABLE_12=value12 --defaults -p
pexpect-executor --delay-press 0.2 \
    --enter \
    --down --enter \
    --down --down --enter \
    --down --down --enter \
    --press 'input' --enter \
    --press '_default' --enter \
    --down --enter \
    --down --enter \
    --down --enter \
    --down --down --enter \
    --enter \
    -- gitlabci-local -e VARIABLE_8=value8 -e VARIABLE_12=value12 -p
pexpect-executor \
    --enter \
    --ctrl c \
    -- gitlabci-local -p && exit -1 || true
