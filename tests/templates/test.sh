#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local 'Job 1' 'Job 2' 'Job 3'
gitlabci-local -B -A 'Job 1' 'Job 2' 'Job 3'
