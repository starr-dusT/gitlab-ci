#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
timeout 5 gitlabci-local -c ./.gitlab-ci.incomplete.yml -p && exit 1 || true
timeout 5 gitlabci-local -c ./.gitlab-ci.incomplete.yml -p --sockets
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml --dump
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml 'Job 1'
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml 'Job 2' && exit 1 || true
timeout 5 gitlabci-local -c ./.gitlab-ci.specific.yml -p
timeout 5 gitlabci-local -c ./.gitlab-ci.specific.yml --dump
