#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local unknown_job && exit 1 || true
gitlabci-local -p unknown_stage && exit 1 || true
gitlabci-local -p && exit 1 || true
gitlabci-local -p one two
gitlabci-local -s -p one two </dev/null
