#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local </dev/null && exit 1 || true
gitlabci-local -p
gitlabci-local --all </dev/null
gitlabci-local -q -p
gcil -p
timeout 5 gitlabci-local 'Job 1' --bash && exit 1 || true
timeout 5 gitlabci-local 'Job 1' --debug && exit 1 || true
gcil Job
gcil 1
gcil 4 && exit 1 || true
