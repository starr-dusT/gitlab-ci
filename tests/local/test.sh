#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local
gitlabci-local -p
gitlabci-local 'Job 1'
gitlabci-local -p local_first
gitlabci-local -n bridge 'Job 2'
gitlabci-local -n host 'Job 2'
gitlabci-local -n none 'Job 2'
