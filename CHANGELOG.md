
<a name="1.1.3"></a>
## [1.1.3](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.2...1.1.3) (2020-03-10)

### CHANGELOG

* regenerate release tag changes history

### Chore

* add 'Dependencies' development requirements local job

### Feat

* implement [#59](https://gitlab.com/AdrianDC/gitlabci-local/issues/59): add support for bash in debug mode
* implement [#60](https://gitlab.com/AdrianDC/gitlabci-local/issues/60): adapt debug command if bash exists

### Fix

* implement [#61](https://gitlab.com/AdrianDC/gitlabci-local/issues/61): handle before_script and after_script like CI
* resolve Python codestyle with YAPF in parser and runner


<a name="1.1.2"></a>
## [1.1.2](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.1...1.1.2) (2020-03-07)

### CHANGELOG

* regenerate release tag changes history

### Fix

* tests: minor local test output syntax cleanup
* finish [#57](https://gitlab.com/AdrianDC/gitlabci-local/issues/57): ensure --debug works upon runner failures too


<a name="1.1.1"></a>
## [1.1.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.0...1.1.1) (2020-03-03)

### CHANGELOG

* regenerate release tag changes history

### Feat

* implement [#57](https://gitlab.com/AdrianDC/gitlabci-local/issues/57): add --debug support to keep runner execution
* implement [#58](https://gitlab.com/AdrianDC/gitlabci-local/issues/58): handle SIGTERM as an interruption


<a name="1.1.0"></a>
## [1.1.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.0.5...1.1.0) (2020-02-23)

### CHANGELOG

* regenerate release tag changes history
* regenerate release tag changes history

### Chore

* finish [#48](https://gitlab.com/AdrianDC/gitlabci-local/issues/48): add missing '.local:network' mention in README
* regenerate preview GIF documentation
* finish [#56](https://gitlab.com/AdrianDC/gitlabci-local/issues/56): cleanup supported .gitlab-ci.yml features
* refresh the README usage helper parameters list
* fix the README and helper tool name to 'gitlabci-local'
* finish [#54](https://gitlab.com/AdrianDC/gitlabci-local/issues/54): add missing tests/includes unit tests call
* resolve [#56](https://gitlab.com/AdrianDC/gitlabci-local/issues/56): document all supported .gitlab-ci.yml features
* finish [#47](https://gitlab.com/AdrianDC/gitlabci-local/issues/47): add '.local:env' mention in README.md
* refresh preview GIF for latest features and parameters
* remove unused configurations variable in parser.py
* ensure Unit Tests jobs timeout after 10 minutes
* resolve colored codestyle with YAPF

### Docs

* regenerate preview GIF with latest changes for 'failures'

### Feat

* add support for 'names' in .local node configurations
* add support for 'when:' result details for clarity
* study [#55](https://gitlab.com/AdrianDC/gitlabci-local/issues/55): add 'Unit Tests (PyPI)' manual customized job
* implement [#54](https://gitlab.com/AdrianDC/gitlabci-local/issues/54): initial support for include:local nodes
* resolve [#47](https://gitlab.com/AdrianDC/gitlabci-local/issues/47): add support for env parsing in .local node
* implement [#50](https://gitlab.com/AdrianDC/gitlabci-local/issues/50): always enable before/after_script by default
* resolve [#52](https://gitlab.com/AdrianDC/gitlabci-local/issues/52): expand volume paths containing variables
* implement [#48](https://gitlab.com/AdrianDC/gitlabci-local/issues/48): add support for a network mode configuration
* implement [#46](https://gitlab.com/AdrianDC/gitlabci-local/issues/46): implement most parameters in .local nodes

### Fix

* resolve [#55](https://gitlab.com/AdrianDC/gitlabci-local/issues/55): use stable docker:19.03.5-dind image service
* resolve [#53](https://gitlab.com/AdrianDC/gitlabci-local/issues/53): parse complete context before parsing stages
* resolve [#51](https://gitlab.com/AdrianDC/gitlabci-local/issues/51): handle global variables as default values only
* resolve [#49](https://gitlab.com/AdrianDC/gitlabci-local/issues/49): preserve environment variables when set in .env


<a name="1.0.5"></a>
## [1.0.5](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.0.4...1.0.5) (2020-01-28)

### CHANGELOG

* regenerate release tag changes history

### Chore

* changelog: add current commit hint with git describe
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): add 'winpty' references for Windows in README
* resolve [#44](https://gitlab.com/AdrianDC/gitlabci-local/issues/44): restrict Python to versions 3.6, 3.7 and 3.8
* setup: add 'Documentation' reference to README.md
* prepare [#44](https://gitlab.com/AdrianDC/gitlabci-local/issues/44): add Python 3.6, 3.7, 3.8 and local tests
* requirements: rename _dev.txt to requirements-dev.txt
* docs: refactor preview.sh Executor class with constants
* tests: add --pull feature validation upon entrypoints test
* gitlab-ci: isolate local preparation jobs to prepare stage

### Feat

* implement [#43](https://gitlab.com/AdrianDC/gitlabci-local/issues/43): allow enabling all jobs with --all
* implement [#41](https://gitlab.com/AdrianDC/gitlabci-local/issues/41): add support for local volumes definitions
* prepare [#41](https://gitlab.com/AdrianDC/gitlabci-local/issues/41): support overriding a bound volume with another
* prepare [#41](https://gitlab.com/AdrianDC/gitlabci-local/issues/41): add support for :ro and :rw volume mounts flags
* implement [#42](https://gitlab.com/AdrianDC/gitlabci-local/issues/42): disable configurations with --defaults
* implement [#40](https://gitlab.com/AdrianDC/gitlabci-local/issues/40): migrate to .local unified configurations node

### Fix

* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): migrate from Blessings to Colored library


<a name="1.0.4"></a>
## [1.0.4](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.0.3...1.0.4) (2020-01-26)

### CHANGELOG

* regenerate release tag changes history

### Chore

* codestyle: pass all Python files through unify with "'"
* codestyle: pass all Python sources through YAPF
* codestyle: add an automated YAPF local job wrapper
* requirements: add YAPF as a development requirement
* requirements: unify and add missing developement items
* development: only rebuild in the Development local stage

### Feat

* implement [#3](https://gitlab.com/AdrianDC/gitlabci-local/issues/3): support job retry values upon executions
* implement [#38](https://gitlab.com/AdrianDC/gitlabci-local/issues/38): pull Docker images if missing upon execution
* implement [#37](https://gitlab.com/AdrianDC/gitlabci-local/issues/37): use low-level Docker pull with streamed logs
* implement [#32](https://gitlab.com/AdrianDC/gitlabci-local/issues/32): add --pull mode for Docker images

### Fix

* resolve [#4](https://gitlab.com/AdrianDC/gitlabci-local/issues/4): fix list view separator in PyInquirer
* resolve [#39](https://gitlab.com/AdrianDC/gitlabci-local/issues/39): resolve Docker Python random exceptions
* resolve [#36](https://gitlab.com/AdrianDC/gitlabci-local/issues/36): support overriding image entrypoint with none
* resolve [#31](https://gitlab.com/AdrianDC/gitlabci-local/issues/31): hardcode the README GIF preview with tags
* resolve [#36](https://gitlab.com/AdrianDC/gitlabci-local/issues/36): preserve original image and CI YAML entrypoints
* resolve [#33](https://gitlab.com/AdrianDC/gitlabci-local/issues/33) support integer variables definitiionz type
* resolve [#13](https://gitlab.com/AdrianDC/gitlabci-local/issues/13): fix rare container wait random failures

### README

* resolve Changelog job reference for 'image: local'
* add pexpect references for docs/ automated preview script


<a name="1.0.3"></a>
## [1.0.3](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.0.2...1.0.3) (2020-01-23)

### CHANGELOG

* regenerate release tag changes history
* implement [#20](https://gitlab.com/AdrianDC/gitlabci-local/issues/20): automate tag and log regeneration

### Chore

* resolve [#15](https://gitlab.com/AdrianDC/gitlabci-local/issues/15): document the .configurations features
* implement [#27](https://gitlab.com/AdrianDC/gitlabci-local/issues/27): add local build and test wrapper

### Feat

* implement [#30](https://gitlab.com/AdrianDC/gitlabci-local/issues/30): add support for working directory parameter
* implement [#29](https://gitlab.com/AdrianDC/gitlabci-local/issues/29): add support for specific volume mounts
* implement [#28](https://gitlab.com/AdrianDC/gitlabci-local/issues/28): add support for specific environment files
* implement [#22](https://gitlab.com/AdrianDC/gitlabci-local/issues/22): add support for passing environment variables
* resolve [#25](https://gitlab.com/AdrianDC/gitlabci-local/issues/25): use listed values for -t tags parameters
* implement [#23](https://gitlab.com/AdrianDC/gitlabci-local/issues/23): add support for native local jobs execution
* implement [#19](https://gitlab.com/AdrianDC/gitlabci-local/issues/19): add support for YAML and JSON configurations
* implement [#16](https://gitlab.com/AdrianDC/gitlabci-local/issues/16): configure with environment variables if set
* implement [#18](https://gitlab.com/AdrianDC/gitlabci-local/issues/18): extend user configurations support for types

### Fix

* resolve [#26](https://gitlab.com/AdrianDC/gitlabci-local/issues/26): use .env variables only as default values
* fix [#25](https://gitlab.com/AdrianDC/gitlabci-local/issues/25): prevent tags parameters from appending default tags
* resolve [#21](https://gitlab.com/AdrianDC/gitlabci-local/issues/21): stop Docker container upon user interruption
* resolve [#17](https://gitlab.com/AdrianDC/gitlabci-local/issues/17): support user interruptions

### README

* resolve [#24](https://gitlab.com/AdrianDC/gitlabci-local/issues/24): document special usage cases


<a name="1.0.2"></a>
## [1.0.2](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.0.1...1.0.2) (2020-01-21)

### CHANGELOG

* implement [#11](https://gitlab.com/AdrianDC/gitlabci-local/issues/11): create initial CHANGELOG with git-chglog

### Chore

* resolve [#12](https://gitlab.com/AdrianDC/gitlabci-local/issues/12): apply VSCode, MarkdownLint and YAPF settings
* implement [#9](https://gitlab.com/AdrianDC/gitlabci-local/issues/9): unify dependencies under requirements.txt

### Docs

* regenerate preview documentations and fix quotes

### Feat

* implement [#11](https://gitlab.com/AdrianDC/gitlabci-local/issues/11): add Changelog link on PyPI releases
* implement [#10](https://gitlab.com/AdrianDC/gitlabci-local/issues/10): support local job tag as being manual jobs
* implement [#7](https://gitlab.com/AdrianDC/gitlabci-local/issues/7): load .env local environment variables
* resolve [#6](https://gitlab.com/AdrianDC/gitlabci-local/issues/6): allow menu selections while using --pipeline

### Fix

* implement [#1](https://gitlab.com/AdrianDC/gitlabci-local/issues/1): add --manual-tags default values documentation
* resolve [#8](https://gitlab.com/AdrianDC/gitlabci-local/issues/8): ensure Docker and other dependencies are recent

### README

* resolve [#5](https://gitlab.com/AdrianDC/gitlabci-local/issues/5): add dependencies list and purposes


<a name="1.0.1"></a>
## [1.0.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.0.0...1.0.1) (2020-01-20)

### Feat

* implement [#2](https://gitlab.com/AdrianDC/gitlabci-local/issues/2): add .configurations dynamic user choices


<a name="1.0.0"></a>
## 1.0.0 (2020-01-18)

