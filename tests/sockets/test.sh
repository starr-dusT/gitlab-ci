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
if [ ! -z "${DOCKER_HOST}" ] && echo "${DOCKER_HOST}" | grep -q '^tcp://'; then
  docker_hostname=$(echo "${DOCKER_HOST}" | sed 's#tcp://\(.*\):.*#\1#')
  docker_ip=$(getent ahostsv4 "${docker_hostname}" | head -n1 | cut -d' ' -f1)
  export DOCKER_HOST=$(echo "${DOCKER_HOST}" | sed "s#${docker_hostname}#${docker_ip}#g")
fi

# Run tests (incomplete)
gitlabci-local -c ./.gitlab-ci.incomplete.yml --dump
gitlabci-local -c ./.gitlab-ci.incomplete.yml --pull
timeout 5 gitlabci-local -c ./.gitlab-ci.incomplete.yml -p && exit 1 || true
timeout 5 gitlabci-local -c ./.gitlab-ci.incomplete.yml -p --sockets

# Run tests (global)
gitlabci-local -c ./.gitlab-ci.global.yml --dump
gitlabci-local -c ./.gitlab-ci.global.yml --pull
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml 'Job 1'
timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml 'Job 2' && exit 1 || true

# Run tests (environment)
DOCKER_CERT_PATH="${DOCKER_CERT_PATH}" DOCKER_TLS_VERIFY="${DOCKER_TLS_VERIFY}" timeout 5 gitlabci-local -c ./.gitlab-ci.global.yml 'Job 1' || true

# Run tests (specific)
gitlabci-local -c ./.gitlab-ci.specific.yml --dump
gitlabci-local -c ./.gitlab-ci.specific.yml --pull
timeout 5 gitlabci-local -c ./.gitlab-ci.specific.yml -p

# Run tests (custom)
gitlabci-local -c ./.gitlab-ci.custom.yml --dump
gitlabci-local -c ./.gitlab-ci.custom.yml --pull
timeout 5 gitlabci-local -c ./.gitlab-ci.custom.yml -p
timeout 5 gitlabci-local -c ./.gitlab-ci.custom.yml 'Job 2' && exit 1 || true
