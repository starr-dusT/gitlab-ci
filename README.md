# gitlabci-local

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

![preview.gif](https://gitlab.com/AdrianDC/gitlabci-local/raw/2.0.0/docs/preview.gif)

---

## Usage

```shell
usage: gitlabci-local [-h] [--version] [-q] [-c CONFIGURATION] [-B] [-A] [-m] [-n NETWORK]
                      [-p] [-e ENV] [-E ENGINE] [-H] [-R] [-t TAGS] [-r] [-S] [-v VOLUME]
                      [-w WORKDIR] [--all] [--defaults] [--bash | --debug]
                      [-d | -s | -l | --pull]
                      [names [names ...]]

gitlabci-local: Launch .gitlab-ci.yml jobs locally (aliases: gcil)
```

| positional arguments |                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------- |
| names                | Names of specific jobs (or stages with --pipeline)<br>Regex names are supported unless --no-regex is used |

| optional arguments   |                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------- |
| -h, --help           | Show this help message                                                                  |
| --version            | Show the current version                                                                |
| -q, --quiet          | Hide jobs execution context                                                             |
| -c CONFIGURATION     | Path to the .gitlab-ci.yml configuration file or folder                                 |
| -B, --no-before      | Disable before_script executions                                                        |
| -A, --no-after       | Disable after_script executions                                                         |
| -m, --manual         | Allow manual jobs to be used                                                            |
| -n NETWORK           | Configure the network mode used<br>Choices: bridge, host, none. Default: bridge         |
| -p, --pipeline       | Run complete stages rather than jobs                                                    |
| -e ENV               | Define VARIABLE=value, pass VARIABLE or ENV file                                        |
| -E ENGINE            | Force a specific engine (or define CI_LOCAL_ENGINE)<br>Default list: auto,podman,docker |
| -H, --host           | Run all jobs on the host rather than containers                                         |
| -R, --no-regex       | Disable regex search of names                                                           |
| -t TAGS              | Handle listed tags as manual jobs<br>Default list: deploy,local,publish                 |
| -r, --real-paths     | Mount real folder paths in the container (Linux only)                                   |
| -S, --sockets        | Mount engine sockets for nested containers                                              |
| -v VOLUME            | Mount VOLUME or HOST:TARGET in containers                                               |
| -w WORKDIR           | Override the container's working path                                                   |
| --all                | Enable all jobs by default in selections                                                |
| --defaults           | Use default variables for .local:configurations                                         |
| --bash               | Prepare runners for manual bash purposes                                                |
| --debug              | Keep runners active for debugging purposes                                              |
| -d, --dump           | Dump parsed .gitlab-ci.yml configuration                                                |
| -s, --select         | Force jobs selection from enumerated names                                              |
| -l, --list           | Select one job to run (implies --manual)                                                |
| --pull               | Pull container images from all jobs                                                     |

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

---

## Supported container engines

gitlabci-local currently supports these container engines:

- **Docker :** https://docs.docker.com/get-docker/ (root daemon, as user or sudoer)
- **Podman :** https://podman.io/getting-started/ (rootless or root CLI)

---

## Supported operating systems

- **Linux systems :**

| Engines               | Linux Mint,  Ubuntu | CentOS | Others |
|:---------------------:|:-------------------:|:------:|:------:|
| Docker (as&nbsp;user) | **✓**               | **✓**  | **?**  |
| Docker (as&nbsp;root) | **✓**               | **✓**  | **?**  |
| Podman (as&nbsp;user) | **~**               | **~**  | **?**  |
| Podman (as&nbsp;root) | **✓**               | **✓**  | **?**  |

- **Windows systems :**

| Engines                | Windows 10 (1909, 2004, 20H2) | Others |
|:----------------------:|:-----------------------------:|:------:|
| Docker (Hyper&#8209;V) | **✓**                         | **?**  |
| Docker (WSL&nbsp;2)    | **✓**                         | **?**  |

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

variables:
  - VARIABLES: VALUES

stages:
  - STAGE_NAMES

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

---

## References

- [.gitlab-ci.yml](https://docs.gitlab.com/ee/ci/yaml/): GitLab CI/CD Pipeline Configuration Reference
- [git-chglog](https://github.com/git-chglog/git-chglog): CHANGELOG generator
- [OCI](https://opencontainers.org): Open Container Initiative
- [peek](https://github.com/phw/peek): Simple GIF screen recorder
- [pexpect](https://pypi.org/project/pexpect/): Interactive console applications controller
- [PyPI](https://pypi.org/): The Python Package Index
- [winpty](https://github.com/rprichard/winpty): Windows PTY interface wrapper
