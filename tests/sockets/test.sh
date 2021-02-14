#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Detect engines
engine_docker=$(
  (type docker >/dev/null 2>&1 && timeout 5 docker --help | grep -iq 'Docker version' && echo 'true') \
    || (curl -s -o /dev/null "${DOCKER_HOST##*/}" && echo 'true') \
    || true
)

# Non-Docker hosts
if [ -z "${engine_docker}" ]; then
  echo 'WARNING: The sockets tests are ignored on non-Docker hosts'
  exit 0
fi

# Configure Docker
if [ ! -z "${DOCKER_HOST}" ]; then
  export DOCKER_HOST=$(echo "${DOCKER_HOST}" | sed 's/docker/172.17.0.1/g')
fi

# Run tests
timeout 5 gitlabci-local -c ./.gitlab-ci.incomplete.yml --dump
timeout 5 gitlabci-local -c ./.gitlab-ci.incomplete.yml -p && exit 1 || true
timeout 5 gitlabci-local -c ./.gitlab-ci.incomplete.yml -p --sockets
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml --dump
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml 'Job 1'
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml 'Job 2' && exit 1 || true
timeout 5 gitlabci-local -c ./.gitlab-ci.specific.yml -p
timeout 5 gitlabci-local -c ./.gitlab-ci.specific.yml --dump
