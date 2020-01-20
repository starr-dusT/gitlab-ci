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

| optional arguments                        |                                           |
| ----------------------------------------- | ----------------------------------------- |
| -h                                        | Show this help message                    |
| -q, --quiet                               | Hide jobs execution context               |
| -c CONFIGURATION                          | Path to the .gitlab-ci.yml configuration  |
| -b, --before                              | Enable before_script executions           |
| -a, --after                               | Enable after_script executions            |
| -m, --manual                              | Allow manual jobs to be used              |
| -t MANUAL_TAGS, --manual-tags MANUAL_TAGS | Handle specific tags as manual jobs       |
| -d, --dump                                | Dump parsed .gitlab-ci.yml configuration  |
| -s, --select                              | Force jobs selection with enumerated jobs |
| -l, --list                                | Select one job to run (implies --manual)  |
| -p, --pipeline                            | Run the pipeline stages without selection |
