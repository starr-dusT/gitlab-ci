#!/usr/bin/env python3

# Standard libraries
from collections import OrderedDict
from os import environ
from os.path import expandvars
from pathlib import Path
from sys import exc_info

# Modules libraries
from dotenv import dotenv_values
from oyaml import safe_load as yaml_safe_load
from oyaml import YAMLError

# Components
from .menu import configurator
from .package.bundle import Bundle
from .prints.colors import Colors

# Reader
def reader(options):

    # Variables
    environment = {
        'default': dict(),
        'files': [],
        'parameters': dict(),
    }

    # Parse environment options
    if options.env:
        for env in options.env:
            env_parsed = env.split('=', 1)

            # Parse VARIABLE=value
            if len(env_parsed) == 2:
                variable = env_parsed[0]
                value = env_parsed[1]
                environ[variable] = value
                environment['parameters'][variable] = value

            # Parse ENVIRONMENT_FILE
            elif (Path(options.path) / env).is_file():
                environment['files'] += [Path(options.path) / env]

            # Parse VARIABLE
            else:
                variable = env
                if variable in environ:
                    environment['parameters'][variable] = environ[variable]
                else:
                    environment['parameters'][variable] = ''

    # Iterate through environment files
    environment['files'] += [Path(options.path) / '.env']
    for environment_file in environment['files']:
        if not environment_file.is_file():
            continue

        # Parse environment files
        environment_file_values = dotenv_values(dotenv_path=environment_file)
        for variable in environment_file_values:

            # Define default environment variable
            if variable in environment['default']:
                continue
            environment['default'][variable] = environment_file_values[variable]

    # Read GitLab CI YAML
    try:
        with open(options.configuration, 'r') as configuration_data:
            data = yaml_safe_load(configuration_data)
            return parser(options, data, environment)
    except YAMLError as exc:
        print(' ')
        print(' %s%s: %sERROR: %s%s%s' %
              (Colors.GREEN, Bundle.NAME, Colors.RED, Colors.BOLD, exc, Colors.RESET))
        print(' ')
    except KeyboardInterrupt:
        pass
    except:
        print(' ')
        print(' %s%s: %sERROR: %s%s%s' % (Colors.GREEN, Bundle.NAME, Colors.RED,
                                          Colors.BOLD, str(exc_info()[1]), Colors.RESET))
        print(' ')

    # Failure
    return None

# Parser
def parser(options, data, environment):

    # Variables
    global_values = dict({
        'after_script': [],
        'before_script': [],
        'image': '',
        'entrypoint': None,
        'variables': dict()
    })
    jobs = dict()
    names_local = False
    stages = dict()

    # Parse nested include
    if 'include' in data and data['include']:
        data_new = dict()
        for include_node in data['include']:

            # Parse local nodes
            if 'local' in include_node:
                file_path = include_node['local'].lstrip('/')
                if (Path(options.path) / file_path).is_file():
                    with open(Path(options.path) / file_path, 'r') as include_data:
                        include_additions = yaml_safe_load(include_data)
                        data_new.update(include_additions)

        # Agregate included data
        data_new.update(data)
        data = data_new
        data_new = None

    # Prepare parameters variables
    if environment['parameters']:
        global_values['variables'].update(environment['parameters'])

    # Filter .local node
    if '.local' in data and data['.local']:
        local = data['.local']

        # Parse local after
        if 'after' in local:
            if options.after:
                options.after = local['after']

        # Parse local all
        if 'all' in local:
            if not options.all:
                options.all = local['all']

        # Parse local bash
        if 'bash' in local:
            if not options.bash:
                options.bash = local['bash']

        # Parse local before
        if 'before' in local:
            if options.before:
                options.before = local['before']

        # Parse local debug
        if 'debug' in local:
            if not options.debug:
                options.debug = local['debug']

        # Parse local defaults
        if 'defaults' in local:
            if not options.defaults:
                options.defaults = local['defaults']

        # Parse local engine
        if 'engine' in local:
            if options.engine_default:
                options.engine = local['engine']
                options.engine_default = False

        # Parse local env
        if 'env' in local:
            for env in local['env']:
                env_parsed = env.split('=', 1)

                # Parse VARIABLE=value
                if len(env_parsed) == 2:
                    variable = env_parsed[0]
                    value = env_parsed[1]
                    if variable not in global_values['variables']:
                        environ[variable] = value
                        global_values['variables'][variable] = value

                # Parse ENVIRONMENT_FILE
                elif (Path(options.path) / env).is_file():
                    environment_file = Path(options.path) / env
                    if not environment_file.is_file():
                        continue

                    # Parse environment files
                    environment_file_values = dotenv_values(dotenv_path=environment_file)
                    for variable in environment_file_values:

                        # Define default environment variable
                        if variable not in global_values['variables']:
                            global_values['variables'][
                                variable] = environment_file_values[variable]

                # Parse VARIABLE
                else:
                    variable = env
                    if variable not in global_values['variables']:
                        if variable in environ:
                            global_values['variables'][variable] = environ[variable]
                        else:
                            global_values['variables'][variable] = ''

        # Parse local image
        if 'image' in local:
            if not options.image:
                options.image = local['image']

        # Parse local manual
        if 'manual' in local:
            if not options.manual:
                options.manual = local['manual']

        # Parse local names
        if 'names' in local:
            if not options.names and not options.pipeline:
                names_local = True
                options.names = local['names']

        # Parse local network
        if 'network' in local:
            if not options.network:
                options.network = local['network']

        # Parse local pipeline
        if 'pipeline' in local:
            if not options.pipeline and (not options.names or names_local):
                options.pipeline = local['pipeline']

        # Parse local quiet
        if 'quiet' in local:
            if not options.quiet:
                options.quiet = local['quiet']

        # Parse local real_paths
        if 'real_paths' in local:
            if not options.real_paths:
                options.real_paths = local['real_paths']

        # Parse local sockets
        if 'sockets' in local:
            if not options.sockets:
                options.sockets = local['sockets']

        # Parse local tags
        if 'tags' in local:
            if options.tags_default:
                options.tags = local['tags'][:]
                options.tags_default = False

        # Parse local volumes
        if 'volumes' in local:
            if not options.volume:
                options.volume = []
            for volume in local['volumes']:
                options.volume += ['.local:' + volume]

        # Parse local workdir
        if 'workdir' in local:
            if not options.workdir:
                options.workdir = '.local:' + local['workdir']

        # Parse local configurations
        if 'configurations' in local:
            configured_variables = configurator(options, local['configurations'])
            global_values['variables'].update(configured_variables)

    # Prepare default variables
    if environment['default']:
        for variable in environment['default']:
            if variable in global_values['variables']:
                pass
            elif variable in environ:
                global_values['variables'][variable] = environ[variable]
            else:
                global_values['variables'][variable] = environment['default'][variable]
            if variable not in environ:
                environ[variable] = global_values['variables'][variable]

    # Prepare global values
    if options.image:
        if isinstance(options.image, dict):
            global_values['image'] = expandvars(options.image['name'])
            if 'entrypoint' in options.image and len(options.image['entrypoint']) > 0:
                global_values['entrypoint'] = options.image['entrypoint'][:]
            else:
                global_values['entrypoint'] = None
        else:
            global_values['image'] = expandvars(options.image)
            global_values['entrypoint'] = None

    # Iterate through nodes
    for node in data:

        # Filter services node
        if node == 'services':
            continue

        # Filter image node
        if node == 'image':
            if not global_values['image']:
                image_data = data[node]
                if isinstance(image_data, dict):
                    global_values['image'] = expandvars(image_data['name'])
                    if 'entrypoint' in image_data and len(image_data['entrypoint']) > 0:
                        global_values['entrypoint'] = image_data['entrypoint'][:]
                    else:
                        global_values['entrypoint'] = None
                else:
                    global_values['image'] = expandvars(image_data)
                    global_values['entrypoint'] = None
            continue

        # Filter before_script node
        if node == 'before_script':
            if isinstance(data[node], str):
                global_values['before_script'] = [data[node]]
            else:
                global_values['before_script'] = data[node]
            continue

        # Filter after_script node
        if node == 'after_script':
            if isinstance(data[node], str):
                global_values['after_script'] = [data[node]]
            else:
                global_values['after_script'] = data[node]
            continue

        # Filter stages node
        if node == 'stages':
            for i, stage in enumerate(data['stages']):
                stages[stage] = i
            continue

        # Filter variables node
        if node == 'variables':
            for variable in data['variables']:
                if variable not in global_values['variables']:
                    if data['variables'][variable] is None:
                        global_values['variables'][variable] = ''
                    else:
                        global_values['variables'][variable] = str(
                            data['variables'][variable])
            continue

    # Prepare environment
    _environ = dict(environ)
    environ.update(global_values['variables'])

    # Iterate through nodes
    for node in data:

        # Ignore global nodes
        if node in [
                'after_script', 'before_script', 'image', 'include', 'stages', 'variables'
        ]:
            continue

        # Validate job node
        if 'stage' not in data[node] and 'extends' not in data[node]:
            continue

        # Ignore template stage
        if node[0:1] == '.':
            continue

        # Register job
        jobs[node] = stager(options, node, data, global_values)

        # Validate job script
        if not jobs[node]['options']['disabled'] and not jobs[node]['script']:
            raise ValueError('Missing "script" key for "%s / %s"' %
                             (jobs[node]['stage'], jobs[node]['name']))

        # Append unknown stage if required
        if jobs[node]['options']['disabled'] and jobs[node][
                'stage'] == 'unknown' and 'unknown' not in stages:
            stages['unknown'] = list(stages.values())[-1] + 1

    # Sort jobs based on stages
    jobs = OrderedDict(sorted(jobs.items(), key=lambda x: stages[x[1]['stage']]))

    # Restore environment
    environ.clear()
    environ.update(_environ)

    # Result
    return jobs

# Stager
def stager(options, job_name, data, global_values):

    # Variables
    job = dict()
    job_data = data[job_name]

    # Prepare stage
    job['name'] = job_name
    job['stage'] = None
    job['image'] = None
    job['entrypoint'] = None
    job['variables'] = None
    job['before_script'] = None
    job['script'] = None
    job['after_script'] = None
    job['retry'] = None
    job['when'] = None
    job['allow_failure'] = None
    job['tags'] = None
    job['trigger'] = None
    job['options'] = dict()
    job['options']['disabled'] = None
    job['options']['host'] = False
    job['options']['quiet'] = False
    job['options']['silent'] = False

    # Extract job extends
    if 'extends' in job_data and job_data['extends']:
        if isinstance(job_data['extends'], list):
            job_extends = job_data['extends']
        else:
            job_extends = [job_data['extends']]

        # Iterate through extended jobs
        for job_extend in reversed(job_extends):

            # Parse extended job
            if job_extend not in data:
                job['options']['disabled'] = '%s unknown' % (job_extend)
                if job['stage'] is None:
                    job['stage'] = 'unknown'
                break
            job_extended = stager(options, job_extend, data, None)

            # Extract extended job
            if job['stage'] is None:
                job['stage'] = job_extended['stage']
            if job['image'] is None:
                job['image'] = job_extended['image']
            if job['entrypoint'] is None:
                job['entrypoint'] = job_extended['entrypoint']
            if job['variables'] is None:
                job['variables'] = job_extended['variables']
            elif job_extended['variables']:
                for variable in job_extended['variables']:
                    if variable not in job['variables']:
                        job['variables'][variable] = job_extended['variables'][variable]
            if job['before_script'] is None:
                job['before_script'] = job_extended['before_script']
            if job['script'] is None:
                job['script'] = job_extended['script']
            if job['after_script'] is None:
                job['after_script'] = job_extended['after_script']
            if job['retry'] is None:
                job['retry'] = job_extended['retry']
            if job['when'] is None:
                job['when'] = job_extended['when']
            if job['allow_failure'] is None:
                job['allow_failure'] = job_extended['allow_failure']
            if job['tags'] is None:
                job['tags'] = job_extended['tags']
            if job['trigger'] is None:
                job['trigger'] = job_extended['trigger']

    # Apply global values
    if global_values:
        if job['image'] is None:
            job['image'] = global_values['image']
        if job['entrypoint'] is None:
            job['entrypoint'] = global_values['entrypoint'][:] if global_values[
                'entrypoint'] else None
        if job['variables'] is None:
            job['variables'] = dict(global_values['variables'])
        else:
            for variable in global_values['variables']:
                if variable not in job['variables']:
                    job['variables'][variable] = global_values['variables'][variable]
        if job['before_script'] is None:
            job['before_script'] = global_values['before_script'][:]
        if job['script'] is None:
            job['script'] = []
        if job['after_script'] is None:
            job['after_script'] = global_values['after_script'][:]
        if job['retry'] is None:
            job['retry'] = 0
        if job['when'] is None:
            job['when'] = 'on_success'
        if job['allow_failure'] is None:
            job['allow_failure'] = False

    # Apply template values
    else:
        if job['variables'] is None:
            job['variables'] = {}

    # Extract job stage
    if 'stage' in job_data and job_data['stage']:
        job['stage'] = job_data['stage']

    # Extract job image
    if 'image' in job_data and job_data['image']:
        image_data = job_data['image']
        if isinstance(image_data, dict):
            job['image'] = expandvars(image_data['name'])
            if 'entrypoint' in image_data and len(image_data['entrypoint']) > 0:
                job['entrypoint'] = image_data['entrypoint'][:]
            else:
                job['entrypoint'] = None
        else:
            job['image'] = expandvars(image_data)
            job['entrypoint'] = None

    # Extract job variables
    if 'variables' in job_data and job_data['variables']:
        for variable in job_data['variables']:
            if job_data['variables'][variable] is None:
                job['variables'][variable] = ''
            else:
                job['variables'][variable] = str(job_data['variables'][variable])

    # Extract job before_script
    if 'before_script' in job_data:
        if job_data['before_script']:
            if isinstance(job_data['before_script'], str):
                job['before_script'] = [job_data['before_script']]
            else:
                job['before_script'] = job_data['before_script'][:]
        else:
            job['before_script'] = []

    # Extract job script
    if 'script' in job_data:
        if job_data['script']:
            if isinstance(job_data['script'], str):
                job['script'] = [job_data['script']]
            else:
                job['script'] = job_data['script'][:]
        else:
            job['script'] = []

    # Extract job after_script
    if 'after_script' in job_data:
        if job_data['after_script']:
            if isinstance(job_data['after_script'], str):
                job['after_script'] = [job_data['after_script']]
            else:
                job['after_script'] = job_data['after_script'][:]
        else:
            job['after_script'] = []

    # Extract job retry
    if 'retry' in job_data:
        retry_data = job_data['retry']
        if isinstance(retry_data, dict):
            job['retry'] = int(retry_data['max'])
        else:
            job['retry'] = int(retry_data)

    # Extract job when
    if 'when' in job_data and job_data['when'] in [
            'on_success', 'on_failure', 'always', 'manual'
    ]:
        job['when'] = job_data['when']

    # Extract job allow_failure
    if 'allow_failure' in job_data and job_data['allow_failure'] in [True, False]:
        job['allow_failure'] = job_data['allow_failure']

    # Extract job tags
    if 'tags' in job_data and job_data['tags']:
        job['tags'] = job_data['tags'][:]

    # Extract job trigger
    if 'trigger' in job_data and job_data['trigger']:
        job['options']['disabled'] = 'trigger only'
        if isinstance(job_data['trigger'], dict):
            job['trigger'] = job_data['trigger']
        elif isinstance(job_data['trigger'], str):
            job['trigger'] = job_data['trigger']

    # Finalize global values
    if global_values:

        # Configure job tags
        if job['tags'] and (set(job['tags']) & set(options.tags)):
            job['when'] = 'manual'

    # Detect host jobs
    if job['image']:
        if job['image'] in ['local', 'local:quiet', 'local:silent']:
            job['options']['host'] = True
        if job['image'] in ['local:quiet', 'local:silent']:
            job['options']['quiet'] = True
        if job['image'] in ['local:silent']:
            job['options']['silent'] = True

    # Result
    return job
