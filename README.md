# gitlabci-local

[![Build](https://gitlab.com/AdrianDC/gitlabci-local/badges/master/pipeline.svg)](https://gitlab.com/AdrianDC/gitlabci-local/-/commits/master/)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=AdrianDC_gitlabci-local&metric=bugs)](https://sonarcloud.io/dashboard?id=AdrianDC_gitlabci-local)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=AdrianDC_gitlabci-local&metric=code_smells)](https://sonarcloud.io/dashboard?id=AdrianDC_gitlabci-local)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=AdrianDC_gitlabci-local&metric=coverage)](https://sonarcloud.io/dashboard?id=AdrianDC_gitlabci-local)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=AdrianDC_gitlabci-local&metric=ncloc)](https://sonarcloud.io/dashboard?id=AdrianDC_gitlabci-local)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AdrianDC_gitlabci-local&metric=alert_status)](https://sonarcloud.io/dashboard?id=AdrianDC_gitlabci-local)

Launch .gitlab-ci.yml jobs locally, wrapped inside the specific images,  
with inplace project volume mounts and adaptive user selections.

---

## Purpose

The main purpose of this project is to unify and enhance reliability  
of builds, tests or releases running on GitLab CI in a similar local context,  
by providing the simplicity of an interactive and automated terminal tool  
and avoiding code duplication (Makefile, Shell scripts, docker run, ...).

Rather than creating yet another standard, the .gitlab-ci.yml specification  
is the common and unique interface between GitLab CI and gitlabci-local.

---

## Preview

![preview.svg](https://gitlab.com/AdrianDC/gitlabci-local/raw/3.1.2/docs/preview.svg)

---

## Examples

| Commands                       | Purpose                                            |
| :----------------------------- | :------------------------------------------------- |
| gitlabci-local                 | Launch the jobs choices interactive menu           |
| gitlabci-local -p              | Launch the jobs pipeline automatically             |
| gitlabci-local -l              | Launch the job selection interactive menu          |
| gitlabci-local 'Dev'           | Launch jobs where the name contains a given string |
| gitlabci-local 'Job 1' --debug | Hold a finishing specific job for debugging        |
| gitlabci-local 'Job 1' --bash  | Prepare a bash environment for a specific job      |
| gcil                           | Shortcut alias to gitlabci-local                   |

---

## Usage

| Command        |                                     |
| -------------- | ----------------------------------- |
| gitlabci-local | Main entrypoint to this project     |
| gcil           | Shortcut entrypoint to this project |

| Internal arguments |                                             |
| ------------------ | ------------------------------------------- |
| -h, --help         | Show this help message                      |
| --version          | Show the current version                    |
| --update-check     | Check for newer package updates             |
| --settings         | Show the current settings path and contents |

| Pipeline arguments |                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| -p, --pipeline     | Automatically run pipeline stages rather than jobs                                              |
| -q, --quiet        | Hide jobs execution context                                                                     |
| -c CONFIGURATION   | Path to the .gitlab-ci.yml configuration file or folder                                         |
| -B, --no-before    | Disable before_script executions                                                                |
| -A, --no-after     | Disable after_script executions                                                                 |
| -n NETWORK         | Configure the network mode used<br>Choices: bridge, host, none. Default: bridge                 |
| -e ENV             | Define VARIABLE=value, pass VARIABLE or ENV file                                                |
| -E ENGINE          | Force a specific engine (or define CI_LOCAL_ENGINE)<br>Default list: auto,podman,docker         |
| -H, --host         | Run all jobs on the host rather than containers                                                 |
| -r, --real-paths   | Mount real folder paths in the container (Linux / macOS only)                                   |
| -S, --sockets      | Mount engine sockets for nested containers<br>(Enabled by default with services: docker:\*dind) |
| -v VOLUME          | Mount VOLUME or HOST:TARGET in containers                                                       |
| -w WORKDIR         | Override the container's working path                                                           |

| Debugging arguments |                                            |
| ------------------- | ------------------------------------------ |
| --bash              | Prepare runners for manual bash purposes   |
| --debug             | Keep runners active for debugging purposes |

| Jobs arguments    |                                                                         |
| ----------------- | ----------------------------------------------------------------------- |
| --all             | Enable all jobs by default in selections                                |
| --defaults        | Use default variables for .local:configurations                         |
| -f, --force       | Force the action (use with --pull)                                      |
| -i, --ignore-case | Ignore case when searching for names                                    |
| -m, --manual      | Allow manual jobs to be used                                            |
| -R, --no-regex    | Disable regex search of names                                           |
| -t TAGS           | Handle listed tags as manual jobs<br>Default list: deploy,local,publish |

| Features arguments |                                            |
| ------------------ | ------------------------------------------ |
| -d, --dump         | Dump parsed .gitlab-ci.yml configuration   |
| -s, --select       | Force jobs selection from enumerated names |
| -l, --list         | Select one job to run (implies --manual)   |
| --pull             | Pull container images from all jobs        |
| --rmi              | Delete container images from all jobs      |

| Positional arguments |                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| names                | Names of specific jobs (or stages with --pipeline)<br>Regex names are supported unless --no-regex is used |

---

## User configurations with ".local:configurations"

gitlabci-local implements support for specific user configurations  
allowing simple and interactive local pipeline configurations.

Supported user configurations include `boolean`, `choice`, `input`, `yaml` and `json`.

Examples for each of these can be found in the `configurations` unit tests: [tests/configurations](https://gitlab.com/AdrianDC/gitlabci-local/blob/master/tests/configurations/.gitlab-ci.yml)

---

## Additional features in ".local"

gitlabci-local implements further support of most parameters  
inside the `.local` to ease default parameters definitions.

Supported local values include `after`, `all`, `bash`, `before`, `configurations`,  
`debug`, `defaults`, `engine`, `env`, `image`, `manual`, `names`, `network`,  
`pipeline`, `quiet`, `real_paths`, `sockets`, `tags`, `volumes`, `workdir`.

Examples for each of these can be found in the `local` unit tests: [tests/local](https://gitlab.com/AdrianDC/gitlabci-local/blob/master/tests/local/.gitlab-ci.yml)

---

## Job execution in native context

gitlabci-local runs every jobs in the specified container image.

For specific local purposes where the native host context is wished,  
where the host tools, folders or credentials are required,  
`image: local` can be used to run the scripts natively.

For specific purposes, the `image: local:quiet` variant  
can be used to enable the `quiet` option for specific jobs.

The `image: local:silent` variant extends the `quiet` option  
by also disabling the verbose script `set -x` line entry.

An example usage can be found in the local `Changelog` job: [.gitlab-ci.yml](https://gitlab.com/AdrianDC/gitlabci-local/blob/master/.gitlab-ci.yml)

---

## Environment variables

gitlabci-local uses the variables defined in .gitlab-ci.yml,  
parses the simple environment variables file named `.env`  
and the configurations selected through `.local:configurations`.

If specific environment variables are to be used in the job's container:

- `-e VARIABLE`: pass an environment variable
- `-e VARIABLE=value`: set a variable to a specific value
- `-e ENVIRONMENT_FILE`: parse a file as default variables

For example, `-e TERM=ansi` may enable colored terminal outputs.

The variable `CI_LOCAL` is automatically defined to `true` by gitlabci-local  
to allow specific conditions for local purposes in jobs' scripts.

The following variables are also defined by gitlabci-local:

- `CI_COMMIT_SHA`: The commit revision for which project is built (GitLab CI)
- `CI_COMMIT_SHORT_SHA`: The first eight characters of CI_COMMIT_SHA (GitLab CI)

---

## Supported container engines

gitlabci-local currently supports these container engines:

- **Docker :** https://docs.docker.com/get-docker/ (root daemon, as user or sudoer)
- **Podman :** https://podman.io/getting-started/ (rootless or root CLI)

---

## Supported Linux systems

|        Engines        | Linux Mint, Ubuntu | CentOS | Others |
| :-------------------: | :----------------: | :----: | :----: |
|    Native (shell)     |       **✓**        | **✓**  | **?**  |
| Docker (as&nbsp;user) |       **✓**        | **✓**  | **?**  |
| Docker (as&nbsp;root) |       **✓**        | **✓**  | **?**  |
| Podman (as&nbsp;user) |       **~**        | **~**  | **?**  |
| Podman (as&nbsp;root) |       **✓**        | **✓**  | **?**  |

---

## Supported macOS systems

|        Engines        | macOS (10.14, 10.15, 11.0, ...) |
| :-------------------: | :-----------------------------: |
|    Native (shell)     |              **✓**              |
| Docker (as&nbsp;user) |              **?**              |

---

## Supported Windows systems

|        Engines         | Windows 10 (1909, 2004, 20H2) | Others |
| :--------------------: | :---------------------------: | :----: |
|     Native (shell)     |             **✓**             | **?**  |
| Docker (Hyper&#8209;V) |             **✓**             | **?**  |
|  Docker (WSL&nbsp;2)   |             **✓**             | **?**  |

---

## Supported Android systems

|     Engines     | Android (7.0, 7.1, 8.0, 8.1, 9.0, 10, 11, ...) |
| :-------------: | :--------------------------------------------: |
| Native (Termux) |                     **✓**                      |

---

## Userspace available settings

gitlabci-local creates a `settings.ini` configuration file in a userspace folder.

For example, it allows to change the default engines priority (`[engines] > engine`),  
or to disable the automated updates daily check (`[updates] > enabled`)

The `settings.ini` file location and contents can be shown with the following command:

```yml
gitlabci-local --settings
```

---

## Supported .gitlab-ci.yml features

```yml
# Global configurations

include:
  local: FILE_PATHS

image: IMAGE_NAME
image:
  name: IMAGE_NAME
  entrypoint: ['COMMANDS']

services:
  - ...docker:dind
  - SERVICE_NAME
  - name: SERVICE_NAME
    alias: SERVICE_ALIAS

stages:
  - STAGE_NAMES

variables:
  - VARIABLES: VALUES

# Global scripts

before_script:
  - COMMANDS

after_script:
  - COMMANDS

# Templates nodes

.TEMPLATES: &TEMPLATES
  KEYS: VALUES

# Job nodes

JOB_NAME:

  # Job configurations

  stage: STAGE_NAME

  image: IMAGE_NAME
  image:
    name: IMAGE_NAME
    entrypoint: ['COMMANDS']

  services:
    - ...docker:dind
    - SERVICE_NAME
    - name: SERVICE_NAME
      alias: SERVICE_ALIAS

  variables:
    VARIABLES: VALUES

  # Job templates

  <<: *TEMPLATES
  extends: TEMPLATE
  extends:
    - TEMPLATES

  # Job scripts

  before_script:
    - COMMANDS

  script:
    - COMMANDS

  after_script:
    - COMMANDS

  # Job executions

  retry: RETRY_COUNT
  retry:
    max: RETRY_COUNT

  tags:
    - MANUAL_TAGS

  trigger: SIMPLE_TRIGGER (ignored)
  trigger:
    COMPLEX_TRIGGER (ignored)

  when: on_success / manual / on_failure / always

  allow_failure: true / false
```

---

## Dependencies

- [colored](https://pypi.org/project/colored/): Terminal colors and styles
- [docker](https://pypi.org/project/docker/): Docker Engine API
- [oyaml](https://pypi.org/project/oyaml/): Ordered YAML dictionnaries
- [PyInquirer](https://pypi.org/project/PyInquirer/): Interactive terminal user interfaces
- [python-dotenv](https://pypi.org/project/python-dotenv/): Support for .env files parsing
- [setuptools](https://pypi.org/project/setuptools/): Build and manage Python packages
- [update-checker](https://pypi.org/project/update-checker/): Check for package updates on PyPI

---

## References

- [.gitlab-ci.yml](https://docs.gitlab.com/ee/ci/yaml/): GitLab CI/CD Pipeline Configuration Reference
- [git-chglog](https://github.com/git-chglog/git-chglog): CHANGELOG generator
- [gitlab-release](https://pypi.org/project/gitlab-release/): Utility for publishing on GitLab
- [OCI](https://opencontainers.org): Open Container Initiative
- [pexpect-executor](https://pypi.org/project/pexpect-executor/): Automate interactive CLI tools actions
- [PyPI](https://pypi.org/): The Python Package Index
- [termtosvg](https://pypi.org/project/termtosvg/): Record terminal sessions as SVG animations
- [Termux](https://termux.com): Linux terminal emulator on Android
- [twine](https://pypi.org/project/twine/): Utility for publishing on PyPI
- [winpty](https://github.com/rprichard/winpty): Windows PTY interface wrapper
