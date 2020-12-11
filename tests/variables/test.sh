#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local -p && exit 1 || true
gitlabci-local -e IMAGE_REFERENCE_1='alpine:3' -p && exit 1 || true
gitlabci-local -e IMAGE_REFERENCE_1='alpine:3' -e IMAGE_REFERENCE_5='alpine:3' -p
