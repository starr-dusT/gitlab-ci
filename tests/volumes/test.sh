#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local -p
gitlabci-local -v ../../tests/volumes:/opt/src:ro -p
gitlabci-local -v ../../tests/volumes:/opt/src:ro -v ../../tests/volumes:/opt/src:ro -p
gitlabci-local -v ../../tests/local:/opt/src:ro -p
gitlabci-local -v ../../tests/volumes:/opt/src3:ro -p
gitlabci-local -v ../../tests/local:/opt/src:ro -v ../../tests/volumes:/opt/src:ro -p && exit 1 || true
gitlabci-local -w . -p
gitlabci-local -r -w . -p
gitlabci-local -w ../../tests/volumes/ -p
gitlabci-local -w /opt/src -p
gitlabci-local -w /opt/unknown -p
gitlabci-local 'Job 2'
gitlabci-local -w . 'Job 2'
gitlabci-local -r 'Job 2'
gitlabci-local -r -w . 'Job 2'
