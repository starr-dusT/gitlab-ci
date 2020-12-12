#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
gitlabci-local --version
gitlabci-local --update-check
COLUMNS=40 gitlabci-local --update-check
CI_LOCAL_UPDATES_OFFLINE=true gitlabci-local --update-check
CI_LOCAL_UPDATES_OFFLINE=true CI_LOCAL_VERSION_FAKE=0.0.2 CI_LOCAL_UPDATES_FAKE=0.0.1 gitlabci-local --update-check
CI_LOCAL_UPDATES_OFFLINE=true CI_LOCAL_VERSION_FAKE=0.0.2 CI_LOCAL_UPDATES_FAKE=0.0.2 gitlabci-local --update-check
CI_LOCAL_UPDATES_OFFLINE=true CI_LOCAL_VERSION_FAKE=0.0.2 CI_LOCAL_UPDATES_FAKE=0.0.3 gitlabci-local --update-check
