
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

