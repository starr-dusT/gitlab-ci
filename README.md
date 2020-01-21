# gitlabci-local

Launch .gitlab-ci.yml jobs locally, wrapped inside the specific images,  
with inplace project volume mounts and adaptive user selections.

---

## Preview

![](https://gitlab.com/AdrianDC/gitlabci-local/raw/master/docs/preview.gif)

---

## Usage

```
usage: gitlabci-runner-local [-h] [-q] [-c CONFIGURATION] [-b] [-a] [-m]
                             [-t MANUAL_TAGS] [-d | -s | -l | -p]
                             [names [names ...]]

gitlabci-runner-local: Launch .gitlab-ci.yml jobs locally
```

| positional arguments |                                                    |
| -------------------- | -------------------------------------------------- |
| names                | Names of specific jobs (or stages with --pipeline) |

| optional arguments |                                             |
| ----------------------------------------- | ------------------------------------------ |
| -h                 | Show this help message                                            |
| -q, --quiet        | Hide jobs execution context                                       |
| -c CONFIGURATION   | Path to the .gitlab-ci.yml configuration                          |
| -b, --before       | Enable before_script executions                                   |
| -a, --after        | Enable after_script executions                                    |
| -m, --manual       | Allow manual jobs to be used                                      |
| -t MANUAL_TAGS     | Handle listed tags as manual jobs<br>Default list: deploy,publish |
| -p, --pipeline     | Run complete stages rather than jobs                              |
| -d, --dump         | Dump parsed .gitlab-ci.yml configuration                          |
| -s, --select       | Force jobs selection from enumerated names                        |
| -l, --list         | Select one job to run (implies --manual)                          |

---

## Dependencies

* [blessings](https://pypi.org/project/blessings/): Terminal colors and styles
* [docker](https://pypi.org/project/docker/): Docker Engine API
* [oyaml](https://pypi.org/project/oyaml/): Ordered YAML dictionnaries
* [PyInquirer](https://pypi.org/project/PyInquirer/): Interactive terminal user interfaces
* [python-dotenv](https://pypi.org/project/python-dotenv/): Support for .env files parsing

---

## References

* [.gitlab-ci.yml](https://docs.gitlab.com/ee/ci/yaml/): GitLab CI/CD Pipeline Configuration Reference
* [peek](https://github.com/phw/peek): Simple GIF screen recorder
* [PyPI](https://pypi.org/): The Python Package Index
