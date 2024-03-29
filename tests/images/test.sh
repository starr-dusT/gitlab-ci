#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local --pull
gitlabci-local --pull
gitlabci-local --pull --force
pexpect-executor -- gitlabci-local --pull --force
gitlabci-local --rmi
gitlabci-local --rmi
gitlabci-local -p
