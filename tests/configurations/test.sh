#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
# gitlabci-local -p && exit 1 || true
gitlabci-local -p </dev/null && exit 1 || true
VARIABLE_8=value8 gitlabci-local -p </dev/null && exit 1 || true
VARIABLE_8= VARIABLE_11=value11 gitlabci-local -p </dev/null
gitlabci-local -e VARIABLE_8=value8 -e VARIABLE_11=value11 -p </dev/null
gitlabci-local -e VARIABLE_8=value8 -e VARIABLE_11=value11 --defaults -p
