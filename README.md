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

![preview.gif](https://gitlab.com/AdrianDC/gitlabci-local/raw/1.0.4/docs/preview.gif)

---

## Usage

```shell
usage: gitlabci-runner-local [-h] [-q] [-c CONFIGURATION] [-b] [-a] [-m] [-p]
                             [-e ENV] [-t TAGS] [-v VOLUME] [-w WORKDIR]
                             [--defaults] [-d | -s | -l | --pull]
                             [names [names ...]]

gitlabci-runner-local: Launch .gitlab-ci.yml jobs locally
```

| positional arguments |                                                    |
| -------------------- | -------------------------------------------------- |
| names                | Names of specific jobs (or stages with --pipeline) |

| optional arguments   |                                                                                   |
| -------------------- | --------------------------------------------------------------------------------- |
| -h                   | Show this help message                                                            |
| -q, --quiet          | Hide jobs execution context                                                       |
| -c CONFIGURATION     | Path to the .gitlab-ci.yml configuration                                          |
| -b, --before         | Enable before_script executions                                                   |
| -a, --after          | Enable after_script executions                                                    |
| -m, --manual         | Allow manual jobs to be used                                                      |
| -e ENV               | Define VARIABLE=value, pass VARIABLE or ENV file                                  |
| -t TAGS              | Handle listed tags as manual jobs<br>Default list: ['deploy', 'local', 'publish'] |
| -p, --pipeline       | Run complete stages rather than jobs                                              |
| -v VOLUME            | Mount VOLUME or HOST:TARGET in Docker containers                                  |
| -w WORKDIR           | Override the container's working path                                             |
| --defaults           | Use default variables for .local:configurations                                   |
| -d, --dump           | Dump parsed .gitlab-ci.yml configuration                                          |
| -s, --select         | Force jobs selection from enumerated names                                        |
| -l, --list           | Select one job to run (implies --manual)                                          |
| --pull               | Pull Docker images from all jobs                                                  |

---

## User configurations with ".local:configurations"

gitlabci-local implements support for specific user configurations  
allowing simple and interactive local pipeline configurations.

Supported user configurations include `boolean`, `choice`, `input`, `yaml` and `json`.

Examples for each of these can be found in the `configurations` unit tests: [tests/configurations](https://gitlab.com/AdrianDC/gitlabci-local/blob/master/tests/configurations/.gitlab-ci.yml)

---

## Job execution in native context

gitlabci-local runs every jobs in the specified Docker image.

For specific local purposes where the native host context is wished,  
where the host tools, folders or credentials are required,  
`image: local` can be used to run the scripts natively.

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

---

## Windows compatibility

In order to access the interactive terminal user interfaces,
Windows users may need to allocate an interactive PTY context
through the `winpty` wrapper, for example `winpty gitlabci-local`.

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
- [peek](https://github.com/phw/peek): Simple GIF screen recorder
- [pexpect](https://pypi.org/project/pexpect/): Interactive console applications controller
- [PyPI](https://pypi.org/): The Python Package Index
- [winpty](https://github.com/rprichard/winpty): Windows PTY interface wrapper
