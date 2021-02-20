#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests (.local)
gitlabci-local -c ./.gitlab-ci.env.yml -p
gitlabci-local -c ./.gitlab-ci.relative.yml -p
gitlabci-local -c ./.gitlab-ci.tilde.yml -p

# Run tests (-v)
gitlabci-local -c ./.gitlab-ci.cli.yml -e USERHOME="${HOME}" -v ~:~ -w ~ -p && exit 1 || true
gitlabci-local -c ./.gitlab-ci.cli.yml -e USERHOME="${HOME}" -v ~:/mnt -w ~ -p
gitlabci-local -c ./.gitlab-ci.cli.yml -e USERHOME="${HOME}" -v "${HOME}:/mnt" -w "${HOME}" -p
