#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local -p && exit 1 || true
gitlabci-local 'Job 1'
gitlabci-local 'Job 2' && exit 1 || true
gitlabci-local 'Job 3' && exit 1 || true
gitlabci-local 'Job 4'
gitlabci-local 'Job 5' && exit 1 || true
gitlabci-local 'Job 6' && exit 1 || true
gitlabci-local 'Job 7'
