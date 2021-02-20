#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
CI_LOCAL_UPDATES_DISABLE= gitlabci-local --version
CI_LOCAL_UPDATES_DISABLE= gitlabci-local --update-check
CI_LOCAL_UPDATES_DISABLE= COLUMNS=40 gitlabci-local --update-check
CI_LOCAL_UPDATES_DISABLE= CI_LOCAL_UPDATES_OFFLINE=true gitlabci-local --update-check
CI_LOCAL_UPDATES_DISABLE= CI_LOCAL_UPDATES_OFFLINE=true CI_LOCAL_VERSION_FAKE=0.0.2 CI_LOCAL_UPDATES_FAKE=0.0.1 gitlabci-local --update-check
CI_LOCAL_UPDATES_DISABLE= CI_LOCAL_UPDATES_OFFLINE=true CI_LOCAL_VERSION_FAKE=0.0.2 CI_LOCAL_UPDATES_FAKE=0.0.2 gitlabci-local --update-check
CI_LOCAL_UPDATES_DISABLE= CI_LOCAL_UPDATES_OFFLINE=true CI_LOCAL_VERSION_FAKE=0.0.2 CI_LOCAL_UPDATES_FAKE=0.0.3 gitlabci-local --update-check
CI_LOCAL_UPDATES_DISABLE= CI_LOCAL_UPDATES_DAILY=true CI_LOCAL_VERSION_FAKE=0.0.2 CI_LOCAL_UPDATES_FAKE=0.0.3 gitlabci-local -H -p
