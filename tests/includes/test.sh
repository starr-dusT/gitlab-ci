#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local -c ./.gitlab-ci.dict.yml -p
gitlabci-local -c ./.gitlab-ci.list.yml -p
gitlabci-local -c ./.gitlab-ci.str.yml -p
