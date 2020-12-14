
<a name="2.3.0"></a>
## [2.3.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.2.3...2.3.0) (2020-12-14)

### Chore

* gitlab-ci: raise interactive tests timeout to 15 minutes
* coverage: ignore unused PyInquirer patcher lines coverage
* tests: add interactive unit tests with pexpect-executor
* docs: resolve configurations test's 12th value support
* lint: isolate and identify 'Modules libraries' imports
* features: prevent YAML dump outputs lines from wrapping
* tests: migrate to pexpect-executor 1.0.1 with tests support
* features: isolate 'dumper' into a 'Jobs' feature
* runner: remove unused engine logs reader and try except
* tests: use 'ubuntu:20.04' for --bash/--debug for bash tests
* tests: add time tests for 60+ seconds pipelines coverage
* tests: add multiple unit tests to improve sources coverage
* parser: handle 'FileNotFoundError' upon file parser
* tests: add unknown configurations test and raise error
* gitlab-ci: unify coverage reports, unify and common scripts
* version: exclude version '0.0.0' fallback from coverage
* gitlab-ci: run coverage and SonarCloud upon tests/ changes
* gitlab-ci: silent and hide all installation irrelevant logs
* tests: add '--settings' specific tests and install 'sudo'
* tests: add missing or incompatible Podman engine tests
* tests: add 'gitlabci-local -i' with regex name tests
* gitlab-ci: remove 'mount' command execution in all tests
* tests: add 'gitlabci-local -c ./folder/' arguments test
* engine: disable the engine.exec command until required
* gitlab-ci: isolate coverage databses and allow suite tests
* gitlab-ci: resolve 'SonarCloud' changes rules on develop
* vscode: exclude intermediate files from the project view
* vscode: migrate to 'brainfit.vscode-coverage-highlighter'
* coverage: ignore coverage of unreachable input securities
* gitlab-ci: implement Python coverage reports for SonarCloud
* gitlab-ci: add 'Py3.9 Preview' test of ./docs/preview.py
* docs: migrate to the isolated 'pexpect-executor' package
* parser: cleanup duplicated environment file checks
* tests: refactor and isolate all unit tests
* version: support non-packaged sources version fallback
* finish [#142](https://gitlab.com/AdrianDC/gitlabci-local/issues/142): isolate pull and rmi into a feature class
* engine: add support for -E '' as being default engines
* tests: add 'engines' tests from arguments and environment
* gitlab-ci: add --settings and wrapped --update-check tests
* gitlab-ci: create YAML anchors to reuse templates scripts
* readme: format the markdown sources automatically
* gitlab-ci: wrap preview.py delay out of the preview script
* requirements: isolate all requirements to a folder
* resolve [#141](https://gitlab.com/AdrianDC/gitlabci-local/issues/141): refactor and fix SonarQube issues for except:
* resolve [#141](https://gitlab.com/AdrianDC/gitlabci-local/issues/141): refactor and fix SonarQube issues in parser

### Feat

* updates: improve updates colors and embed new test flags
* finish [#144](https://gitlab.com/AdrianDC/gitlabci-local/issues/144): add missing regex check for -i case option
* implement [#144](https://gitlab.com/AdrianDC/gitlabci-local/issues/144): add -i to ignore jobs name case distinctions
* implement [#143](https://gitlab.com/AdrianDC/gitlabci-local/issues/143): add --force to force pull container images
* implement [#142](https://gitlab.com/AdrianDC/gitlabci-local/issues/142): add --rmi to remove container images

### Fix

* resolve [#148](https://gitlab.com/AdrianDC/gitlabci-local/issues/148): handle JSON or YAML string as unique choice
* resolve [#146](https://gitlab.com/AdrianDC/gitlabci-local/issues/146): ensure before_script really checks for issues
* resolve [#147](https://gitlab.com/AdrianDC/gitlabci-local/issues/147): default YAML or JSON value if non-interactive
* resolve [#145](https://gitlab.com/AdrianDC/gitlabci-local/issues/145): Handle configurations Dicts index out of range
* finish [#137](https://gitlab.com/AdrianDC/gitlabci-local/issues/137): delete temporary files only if they still exist


<a name="2.2.3"></a>
## [2.2.3](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.2.2...2.2.3) (2020-12-10)

### Chore

* gitlab-ci: resolve Podman 2.2.1 issues in Debian 10.6
* gitlab-ci: prevent Podman unit tests to use Docker host
* readme: add pipeline and SonarCloud badges
* resolve [#141](https://gitlab.com/AdrianDC/gitlabci-local/issues/141): minor codestyle cleanups raised by SonarCloud
* resolve [#141](https://gitlab.com/AdrianDC/gitlabci-local/issues/141): resolve SonarQube issue in engines.wait
* gitlab-ci.yml: add support for SonarCloud analysis
* gitlab-ci: run build and tests jobs only if needed


<a name="2.2.2"></a>
## [2.2.2](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.2.1...2.2.2) (2020-12-09)

### Chore

* gitlab-ci: ignore Podman issues until podman-2.2.1 is fixed
* resolve [#140](https://gitlab.com/AdrianDC/gitlabci-local/issues/140): add 'Platform.IS_ANDROID' unused constant

### Docs

* resolve [#140](https://gitlab.com/AdrianDC/gitlabci-local/issues/140): add Android test environment explanations
* resolve [#140](https://gitlab.com/AdrianDC/gitlabci-local/issues/140): mention Android native engine with Termux
* prepare [#140](https://gitlab.com/AdrianDC/gitlabci-local/issues/140): add installation steps for all test platforms

### Fix

* resolve [#137](https://gitlab.com/AdrianDC/gitlabci-local/issues/137): ensure temporary scripts are always deleted
* resolve [#139](https://gitlab.com/AdrianDC/gitlabci-local/issues/139): support readonly parent folders for entrypoints
* resolve [#138](https://gitlab.com/AdrianDC/gitlabci-local/issues/138): reset colors once the boxes are printed


<a name="2.2.1"></a>
## [2.2.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.2.0...2.2.1) (2020-12-08)

### Chore

* prepare [#135](https://gitlab.com/AdrianDC/gitlabci-local/issues/135): isolate string manipulators to 'Strings' type

### Feat

* resolve [#136](https://gitlab.com/AdrianDC/gitlabci-local/issues/136): adapt update hint to sudo-installed packages

### Fix

* resolve [#135](https://gitlab.com/AdrianDC/gitlabci-local/issues/135): wrap colored strings and adapt boxes dimensions


<a name="2.2.0"></a>
## [2.2.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.1.2...2.2.0) (2020-12-07)

### Chore

* gitlab-ci: implement 'gitlab-release' to fill tags releases
* changelog: create a CHANGELOG version description extractor
* resolve [#134](https://gitlab.com/AdrianDC/gitlabci-local/issues/134): isolate environment variables inside 'Bundle'
* resolve [#134](https://gitlab.com/AdrianDC/gitlabci-local/issues/134): isolate package names to a 'Bundle' class
* prepare [#131](https://gitlab.com/AdrianDC/gitlabci-local/issues/131): add 'REPOSITORY' GitLab URL link constant
* implement [#133](https://gitlab.com/AdrianDC/gitlabci-local/issues/133): isolate all colors attributes into a class
* readme: add 'native' local jobs as supported engine

### Docs

* prepare [#118](https://gitlab.com/AdrianDC/gitlabci-local/issues/118): add supported macOS versions and update TEST

### Feat

* implement [#131](https://gitlab.com/AdrianDC/gitlabci-local/issues/131): refactor the updates message with hints
* prepare [#131](https://gitlab.com/AdrianDC/gitlabci-local/issues/131): create 'Boxes' class to create boxed messages
* implement [#133](https://gitlab.com/AdrianDC/gitlabci-local/issues/133): add 'center' and 'strip' string manipulators
* implement [#131](https://gitlab.com/AdrianDC/gitlabci-local/issues/131): check for updates without delay upon exit
* implement [#132](https://gitlab.com/AdrianDC/gitlabci-local/issues/132): use the original userspace if using sudo
* prepare [#132](https://gitlab.com/AdrianDC/gitlabci-local/issues/132): provide IS_USER_SUDO and USER_SUDO constants


<a name="2.1.2"></a>
## [2.1.2](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.1.1...2.1.2) (2020-12-05)

### Chore

* tests: add 'images' test job for native and container jobs
* types: refactor 'Dicts.find' without regex dependency
* readme: add command usage entrypoint and shortcuts table
* readme: drop the unreadable and old usage short help header
* types: turn 'Paths' class methods into static methods

### Docs

* resolve [#129](https://gitlab.com/AdrianDC/gitlabci-local/issues/129): document the settings configurations and goals

### Feat

* prepare [#129](https://gitlab.com/AdrianDC/gitlabci-local/issues/129): add '--settings' to show the path and contents

### Fix

* resolve [#130](https://gitlab.com/AdrianDC/gitlabci-local/issues/130): respect list selector single choice inputs
* resolve [#129](https://gitlab.com/AdrianDC/gitlabci-local/issues/129): import modules libraries before components


<a name="2.1.1"></a>
## [2.1.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.1.0...2.1.1) (2020-12-05)

### Chore

* vscode: disable terminal app insights telemetry
* vscode: ensure YAML use single quotes formatting
* vscode: add recommended VSCode extensions list
* vscode: always format files upon editor saves
* vscode: configure VSCode telemetry and privacy settings

### Docs

* prepare [#118](https://gitlab.com/AdrianDC/gitlabci-local/issues/118): add macOS references in README and TEST

### Feat

* implement [#128](https://gitlab.com/AdrianDC/gitlabci-local/issues/128): store and read default engines in settings
* resolve [#122](https://gitlab.com/AdrianDC/gitlabci-local/issues/122): add CI_JOB_NAME and CI_PROJECT_DIR definitions
* prepare [#122](https://gitlab.com/AdrianDC/gitlabci-local/issues/122): allow expanding CI_LOCAL in variables values
* prepare [#118](https://gitlab.com/AdrianDC/gitlabci-local/issues/118): support macOS paths, userspace and real paths
* prepare [#118](https://gitlab.com/AdrianDC/gitlabci-local/issues/118): add Platform.IS_MAC_OS platform detection
* prepare [#118](https://gitlab.com/AdrianDC/gitlabci-local/issues/118): restrict Docker sockets mounts to Linux only

### Fix

* prepare [#121](https://gitlab.com/AdrianDC/gitlabci-local/issues/121): isolate print flushes and allow only on TTY out
* resolve [#127](https://gitlab.com/AdrianDC/gitlabci-local/issues/127): evaluate host project directories correctly

### Tests

* validate [#122](https://gitlab.com/AdrianDC/gitlabci-local/issues/122): create specific test cases for CI projects


<a name="2.1.0"></a>
## [2.1.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.0.1...2.1.0) (2020-12-03)

### Chore

* resolve [#123](https://gitlab.com/AdrianDC/gitlabci-local/issues/123): isolate into classes and lint the sources
* gitlab-ci: isolate pip install steps in 'before_script'
* prepare [#123](https://gitlab.com/AdrianDC/gitlabci-local/issues/123): import only required libraries in setup.py
* prepare [#123](https://gitlab.com/AdrianDC/gitlabci-local/issues/123): import only required libraries in preview.py
* gitlab-ci: add local 'Lint' job as a pylint wrapper
* gitlab-ci: disable pip updates warnings in relevant jobs
* gitlab-ci: turn the 'Codestyle' job into a CI check job
* gitlab-ci: quiet pip installation logs in 'deploy' jobs
* gitlab-ci: isolate local jobs under a 'development' stage
* gitlab-ci: isolate requirements and use built packages
* gitlab-ci: add '--force-reinstall' to pip reinstallations

### Feat

* implement [#124](https://gitlab.com/AdrianDC/gitlabci-local/issues/124): add daily PyPI updates notifications
* implement [#125](https://gitlab.com/AdrianDC/gitlabci-local/issues/125): implement a settings storage class
* implement [#126](https://gitlab.com/AdrianDC/gitlabci-local/issues/126): add network mode support in Podman engine


<a name="2.0.1"></a>
## [2.0.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/2.0.0...2.0.1) (2020-12-01)

### Chore

* readme: isolate Linux and Windows tables in chapters
* readme: minor missing line break in native context jobs
* gitlab-ci: use 'Deploy Trial' name to avoid 'Test' issues
* gitlab-ci: add 'Preview' wrapper job for 'docs/preview.py'
* resolve [#111](https://gitlab.com/AdrianDC/gitlabci-local/issues/111): improve '-p' pipeline documentation details
* resolve [#112](https://gitlab.com/AdrianDC/gitlabci-local/issues/112): prevent line break of 'Hyper-V' in engines
* resolve [#119](https://gitlab.com/AdrianDC/gitlabci-local/issues/119): avoid preparing volumes on native jobs
* resolve [#112](https://gitlab.com/AdrianDC/gitlabci-local/issues/112): prevent line breaks in the tables
* resolve [#111](https://gitlab.com/AdrianDC/gitlabci-local/issues/111): cleanup typos and improve --help details

### Docs

* resolve [#117](https://gitlab.com/AdrianDC/gitlabci-local/issues/117): add usual examples of parameters
* resolve [#120](https://gitlab.com/AdrianDC/gitlabci-local/issues/120): refactor the supported .gitlab-ci.yml nodes
* readme: add Windows 10 1909 as being a supported system
* test: add tools and engines references for Linux and Windows

### Feat

* resolve [#113](https://gitlab.com/AdrianDC/gitlabci-local/issues/113): standardize --tags values as "list,of,values"

### Fix

* resolve [#116](https://gitlab.com/AdrianDC/gitlabci-local/issues/116): fix native scripts working directory access
* resolve [#114](https://gitlab.com/AdrianDC/gitlabci-local/issues/114): show default prioritized engines list in --help


<a name="2.0.0"></a>
## [2.0.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.3.1...2.0.0) (2020-11-30)

### Chore

* gitlab-ci: add Test PyPI uploader local manual job
* docs: refresh the preview GIF for the latest 2.0.0 release
* docs: use Docker engine by default and minor cleanups
* docs: drop 'gitlabci-local --help' command in the preview
* gitignore: exclude all .tmp.* entrypoint intermediate files
* gitlab-ci: add 'pwd' and 'mount' to all tests jobs
* gitlab-ci: use the Docker engine by default for development
* run: add 'run.sh' script for local development purposes
* gitlab-ci: avoid reinstalling upon local native tests
* gitlab-ci: resolve colored terminal outputs in 'Test'
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): isolate /builds and /tmp paths in const class
* main: use a global variable for '.gitlab-ci.yml' file name
* gitlab-ci: install production requirements then development
* gitlab-ci: add command headers for the 'Test' local job
* gitlab-ci: add 'git --name-status' after 'Codestyle' fixes
* gitlab-ci: add 'Test' local job to run unit tests suites
* resolve [#86](https://gitlab.com/AdrianDC/gitlabci-local/issues/86): hide irrelevant internal values from --dump
* development: install as 'sudoer' when using 'Development'
* gitlab-ci: ensure /usr/local/path is in PATH for all tests
* prepare [#82](https://gitlab.com/AdrianDC/gitlabci-local/issues/82): ensure Python 3 is explicitly used in 'Deploy'
* dev: add missing setuptools-scm development requirement
* prepare [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): reduce Docker specific references and add OCI
* prepare [#82](https://gitlab.com/AdrianDC/gitlabci-local/issues/82): ensure Python 3 is explicitly used in 'Build'

### Docs

* readme: center operating systems and engines names tables
* gitlab-ci: use 'docs: changelog:' for changelog commits
* readme: improve readability of supported engines and systems
* readme: refresh 'gitlabci-local' usage and parameters lists
* document [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): add supported systems and engines in README

### Feat

* resolve [#108](https://gitlab.com/AdrianDC/gitlabci-local/issues/108): define CI_LOCAL_ENGINE if engine option is set
* resolve [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): automate interactive winpty calls on Windows
* implement [#101](https://gitlab.com/AdrianDC/gitlabci-local/issues/101): add '-S' to manually mount engine sockets
* implement [#103](https://gitlab.com/AdrianDC/gitlabci-local/issues/103): see the used engine in the job header
* resolve [#100](https://gitlab.com/AdrianDC/gitlabci-local/issues/100): add '.local: real_paths:' configuration
* resolve [#100](https://gitlab.com/AdrianDC/gitlabci-local/issues/100): use /builds paths for the temporary script
* resolve [#100](https://gitlab.com/AdrianDC/gitlabci-local/issues/100): use /builds paths and add '-r' for real mounts
* resolve [#99](https://gitlab.com/AdrianDC/gitlabci-local/issues/99): add support and tests for Python 3.9.0
* resolve [#93](https://gitlab.com/AdrianDC/gitlabci-local/issues/93): add 'docker,' / 'podman,' for engines priority
* implement [#92](https://gitlab.com/AdrianDC/gitlabci-local/issues/92): add '.local:engine' default configurations
* finish [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): refactor with Podman subprocess CLI calls
* fix [#85](https://gitlab.com/AdrianDC/gitlabci-local/issues/85): resolve puller access to job options 'host'
* fix [#87](https://gitlab.com/AdrianDC/gitlabci-local/issues/87): use setuptools API for the --version informations
* extend [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): add -E engine selection and add CI_LOCAL_ENGINE
* implement [#89](https://gitlab.com/AdrianDC/gitlabci-local/issues/89): improve pipeline total duration outputs
* implement [#88](https://gitlab.com/AdrianDC/gitlabci-local/issues/88): add 'image: local:silent' as host silent jobs
* implement [#87](https://gitlab.com/AdrianDC/gitlabci-local/issues/87): add support for --version informations
* implement [#85](https://gitlab.com/AdrianDC/gitlabci-local/issues/85): add 'image: local:quiet' for host quiet jobs
* implement [#84](https://gitlab.com/AdrianDC/gitlabci-local/issues/84): accept -c with folder path to .gitlab-ci.yml
* implement [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): add Podman root / sudoers engine support
* finish [#79](https://gitlab.com/AdrianDC/gitlabci-local/issues/79): add 'Statistics' links for PyPI
* implement [#82](https://gitlab.com/AdrianDC/gitlabci-local/issues/82): add -H or --host to force host local usage

### Fix

* gitlab-ci: resolve "${PWD}" path usage with spaces in tests
* resolve [#110](https://gitlab.com/AdrianDC/gitlabci-local/issues/110): fix non-interactive menus and engine on Windows
* resolve [#105](https://gitlab.com/AdrianDC/gitlabci-local/issues/105): handle duplicated source paths on Windows too
* resolve [#107](https://gitlab.com/AdrianDC/gitlabci-local/issues/107): support working directory in local native jobs
* resolve [#106](https://gitlab.com/AdrianDC/gitlabci-local/issues/106): use required pure POSIX paths for workdir paths
* resolve [#109](https://gitlab.com/AdrianDC/gitlabci-local/issues/109): disallow real paths usage on Windows
* resolve [#106](https://gitlab.com/AdrianDC/gitlabci-local/issues/106): resolve relative workdir paths against options
* resolve [#105](https://gitlab.com/AdrianDC/gitlabci-local/issues/105): handle volumes duplicates and local overrides
* resolve [#106](https://gitlab.com/AdrianDC/gitlabci-local/issues/106): resolve relative paths against configuration
* resolve [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): support local script paths with spaces
* resolve [#105](https://gitlab.com/AdrianDC/gitlabci-local/issues/105): support mounting a path twice without overlaps
* resolve [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): use only /builds folder for entrypoint scripts
* resolve [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): use isolated temporary directory to avoid issues
* gitlab-ci: use real paths and bind sockets for development
* gitlab-ci: refactor, nested containers and Podman 3.6 to 3.9
* gitlab-ci: resolve "${PWD}" real path upon environment tests
* resolve [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): avoid using host '/tmp' with container processes
* resolve [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): bind temp directory to avoid Hyper-V share spams
* resolve [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): use 'sh' explicitly for local native scripts
* test [#102](https://gitlab.com/AdrianDC/gitlabci-local/issues/102): test if CI_LOCAL_ENGINE_NAME is defined twice
* resolve [#104](https://gitlab.com/AdrianDC/gitlabci-local/issues/104): configure and instantiate the engine only once
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): resolve 'local: workdir' absolute path in parser
* resolve [#102](https://gitlab.com/AdrianDC/gitlabci-local/issues/102): ensure CI_LOCAL_ENGINE_NAME is set for all jobs
* prepare [#103](https://gitlab.com/AdrianDC/gitlabci-local/issues/103): use hidden internal members in Engine classes
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): resolve workdir absolute path before using it
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): prepare Windows specific changes in resolvePath
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): exclude /var/run/docker.sock from Windows mounts
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): add IS_LINUX and IS_WINDOWS constants
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): remove the temporary script only after execution
* finish [#89](https://gitlab.com/AdrianDC/gitlabci-local/issues/89): minor comments typo fixes upon time evaluations
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): use PurePosixPath for internal container paths
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): use Linux newline endings in entrypoint scripts
* prepare [#34](https://gitlab.com/AdrianDC/gitlabci-local/issues/34): migrate from os.path to pathlib Path items
* resolve [#95](https://gitlab.com/AdrianDC/gitlabci-local/issues/95): avoid opening the NamedTemporaryFile file twice
* resolve [#96](https://gitlab.com/AdrianDC/gitlabci-local/issues/96): support non-regex names like "C++" in inputs
* resolve [#98](https://gitlab.com/AdrianDC/gitlabci-local/issues/98): avoid running incomplete jobs in pipelines
* finish [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): ensure the entrypoint script is user accessible
* finish [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): add '--privileged' flag for Podman containers
* finish [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): avoid CI_LOCAL_ENGINE / CI_LOCAL_ENGINE_NAME loop
* resolve [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): avoid Python 3.7+ specific 'capture_output'
* finish [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): define CI_LOCAL_ENGINE and resolve Podman tests
* test [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): use extends rather than anchos to keeps variables
* resolve [#91](https://gitlab.com/AdrianDC/gitlabci-local/issues/91): fix parser support for empty variables
* resolve [#90](https://gitlab.com/AdrianDC/gitlabci-local/issues/90): fix regex searches of names upon --dump
* gitlab-ci: remove PATH to avoid issues with Docker-in-Docker
* gitlab-ci: add engines sources to the codestyle input files
* gitlab-ci: migrate to Docker-in-Docker (dind) 19.03.13
* implement [#83](https://gitlab.com/AdrianDC/gitlabci-local/issues/83): add support for 'variables:' usage in 'image:'
* prepare [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): add missing 'linux-headers' for the Podman test
* tests: resolve entrypoint i686 / x86_64 unreliable results
* resolve [#81](https://gitlab.com/AdrianDC/gitlabci-local/issues/81): avoid invoking Docker APIs if running local jobs

### Parser

* resolve [#94](https://gitlab.com/AdrianDC/gitlabci-local/issues/94): ignore and consider trigger jobs as disabled

### Refactor

* prepare [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): isolate the Docker engine as an abstract
* prepare [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): isolate Docker engine specific APIs

### Test

* prepare [#105](https://gitlab.com/AdrianDC/gitlabci-local/issues/105): specific tests for local and CLI volumes
* prepare [#80](https://gitlab.com/AdrianDC/gitlabci-local/issues/80): add Podman specific test job for reference


<a name="1.3.1"></a>
## [1.3.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.3.0...1.3.1) (2020-10-23)

### Feat

* resolve [#79](https://gitlab.com/AdrianDC/gitlabci-local/issues/79): add 'Bug Reports' and 'Source' links for PyPI
* implement [#78](https://gitlab.com/AdrianDC/gitlabci-local/issues/78): add total pipeline time in results


<a name="1.3.0"></a>
## [1.3.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.2.1...1.3.0) (2020-10-21)

### Chore

* setup: add support for comments in requirements.txt
* requirements: bind setuptools for delivery rather than dev

### Feat

* resolve [#74](https://gitlab.com/AdrianDC/gitlabci-local/issues/74): disable incomplete jobs instead of failing

### Fix

* resolve [#77](https://gitlab.com/AdrianDC/gitlabci-local/issues/77): resolve standalone multiline scripts parser

### Test

* validate [#77](https://gitlab.com/AdrianDC/gitlabci-local/issues/77): check standalone multiline scripts parser


<a name="1.2.1"></a>
## [1.2.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.2.0...1.2.1) (2020-08-04)

### Chore

* gitlab-ci: remove unnecessary 'tags: local' for local jobs

### Feat

* implement [#73](https://gitlab.com/AdrianDC/gitlabci-local/issues/73): add support for regex searches of names
* resolve [#72](https://gitlab.com/AdrianDC/gitlabci-local/issues/72): add support for the --help parameter along -h
* document [#71](https://gitlab.com/AdrianDC/gitlabci-local/issues/71): add 'gcil' alias references in help and README
* implement [#71](https://gitlab.com/AdrianDC/gitlabci-local/issues/71): add a shorter "gcil" entrypoint wrapper
* implement [#67](https://gitlab.com/AdrianDC/gitlabci-local/issues/67): define CI_LOCAL variable to detect local jobs

### Fix

* resolve [#70](https://gitlab.com/AdrianDC/gitlabci-local/issues/70): support disabling *script: nodes with extends:
* resolve [#69](https://gitlab.com/AdrianDC/gitlabci-local/issues/69): propagate and cumulate extended jobs' variables
* resolve [#68](https://gitlab.com/AdrianDC/gitlabci-local/issues/68): add empty footer lines upon error failures

### Test

* validate [#71](https://gitlab.com/AdrianDC/gitlabci-local/issues/71): check 'gcil' works on the 'simple' tests


<a name="1.2.0"></a>
## [1.2.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.6...1.2.0) (2020-06-13)

### Feat

* implement [#66](https://gitlab.com/AdrianDC/gitlabci-local/issues/66): add support for 'extends' jobs in parser

### Fix

* prepare [#66](https://gitlab.com/AdrianDC/gitlabci-local/issues/66): respect included data order in 'include' nodes
* prepare [#66](https://gitlab.com/AdrianDC/gitlabci-local/issues/66): ensure global keys will not be parsed as jobs
* prepare [#66](https://gitlab.com/AdrianDC/gitlabci-local/issues/66): ensure missing 'script' required node detection
* prepare [#66](https://gitlab.com/AdrianDC/gitlabci-local/issues/66): ensure missing 'image' key is properly detected

### Tests

* validate [#66](https://gitlab.com/AdrianDC/gitlabci-local/issues/66): ensure 'extends' full support is validated


<a name="1.1.6"></a>
## [1.1.6](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.5...1.1.6) (2020-04-02)

### Chore

* validate [#64](https://gitlab.com/AdrianDC/gitlabci-local/issues/64): ensure first failure drops the script

### Feat

* implement [#62](https://gitlab.com/AdrianDC/gitlabci-local/issues/62): add support for 'allow_failure: true' options
* implement [#63](https://gitlab.com/AdrianDC/gitlabci-local/issues/63): add execution timings for every job

### Fix

* resolve [#65](https://gitlab.com/AdrianDC/gitlabci-local/issues/65): synchronize stdout and stderr runner outputs


<a name="1.1.5"></a>
## [1.1.5](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.4...1.1.5) (2020-03-15)

### Chore

* deprecate 'Deploy Test' and enforce automatic tags release

### Fix

* resolve UTF-8 stdout outputs from container logs stream


<a name="1.1.4"></a>
## [1.1.4](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.3...1.1.4) (2020-03-15)

### Fix

* fix [#61](https://gitlab.com/AdrianDC/gitlabci-local/issues/61): handle before_script and script together like CI


<a name="1.1.3"></a>
## [1.1.3](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.2...1.1.3) (2020-03-10)

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

### Fix

* tests: minor local test output syntax cleanup
* finish [#57](https://gitlab.com/AdrianDC/gitlabci-local/issues/57): ensure --debug works upon runner failures too


<a name="1.1.1"></a>
## [1.1.1](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.1.0...1.1.1) (2020-03-03)

### Feat

* implement [#57](https://gitlab.com/AdrianDC/gitlabci-local/issues/57): add --debug support to keep runner execution
* implement [#58](https://gitlab.com/AdrianDC/gitlabci-local/issues/58): handle SIGTERM as an interruption


<a name="1.1.0"></a>
## [1.1.0](https://gitlab.com/AdrianDC/gitlabci-local/compare/1.0.5...1.1.0) (2020-02-23)

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

