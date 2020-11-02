#!/usr/bin/env python3

# Libraries
import colored
import datetime
import os
from pathlib import Path
import signal
import stat
import sys
import tempfile
import time

# Components
from .engine import Engine
from .main import NAME
from .utils import nameCheck

# Constants
marker_debug = '__GITLAB_CI_LOCAL_DEBUG__'
marker_result = '__GITLAB_CI_LOCAL_RESULT__'

# Launcher
def launcher(options, jobs):

    # Variables
    time_launcher = time.time()
    result = None

    # Run selected jobs
    for job in jobs:

        # Filter jobs list
        if not options.pipeline and not nameCheck(job, options.names, options.no_regex):
            continue

        # Filter stages list
        if options.pipeline and options.names and not nameCheck(
                jobs[job]['stage'], options.names, options.no_regex):
            continue

        # Filter manual jobs
        job_manual = (jobs[job]['when'] == 'manual')
        if job_manual and not options.manual and not nameCheck(job, options.names,
                                                               options.no_regex):
            continue

        # Raise initial result
        if result == None:
            result = True

        # Run job
        attempt = 0
        expected = result
        result = runner(options, jobs[job], result, time_launcher)

        # Retry job if allowed
        if expected and not result and jobs[job]['retry'] > 0:
            while not result and attempt < jobs[job]['retry']:
                attempt += 1
                result = runner(options, jobs[job], expected, time_launcher)

    # Result
    return True if result else False

# Runner
def runner(options, job_data, last_result, time_launcher):

    # Variables
    engine = None
    local_runner = False
    result = False
    time_start = time.time()

    # Filter when
    if last_result and job_data['when'] not in ['on_success', 'manual', 'always']:
        return last_result
    if not last_result and job_data['when'] not in ['on_failure']:
        return last_result

    # Prepare image
    image = job_data['image']

    # Prepare local runner
    if options.host or image in ['local']:
        image = 'local'
        local_runner = True

    # Prepare network
    network = 'bridge'
    if options.network:
        network = options.network

    # Header
    if not options.quiet:
        print(' %s===[ %s%s: %s%s %s(%s) %s]===%s' %
              (colored.fg('green') + colored.attr('bold'),
               colored.fg('yellow') + colored.attr('bold'), job_data['stage'],
               colored.fg('yellow') + colored.attr('bold'), job_data['name'],
               colored.fg('cyan') + colored.attr('bold'), image,
               colored.fg('green') + colored.attr('bold'), colored.attr('reset')))
        print(' ', flush=True)

    # Acquire project path
    pathProject = options.path
    pathParent = str(Path(pathProject).parent)

    # Prepare working directory
    if options.workdir:
        pathWorkDir = os.path.abspath(options.workdir)
    else:
        pathWorkDir = pathProject

    # Prepare entrypoint and scripts
    entrypoint = job_data['entrypoint']
    scriptsAfter = []
    scriptsBefore = []
    scriptsCommands = []
    scriptsDebug = []

    # Prepare before_scripts
    if options.before:
        scriptsBefore += job_data['before_script']

    # Prepare scripts
    scriptsCommands += job_data['script']
    if not local_runner:
        if options.bash:
            scriptsCommands = []
        if options.bash or options.debug:
            scriptsDebug += ['echo "' + marker_debug + '"', 'tail -f /dev/null']

    # Prepare after_scripts
    if options.after:
        scriptsAfter += job_data['after_script']

    # Prepare commands
    scriptFile = tempfile.NamedTemporaryFile(delete=True)
    with open(scriptFile.name, mode='w') as scriptStream:

        # Prepare execution context
        scriptStream.write('#!/bin/sh')
        scriptStream.write('\n')
        scriptStream.write('result=1')
        scriptStream.write('\n')

        # Prepare before_script/script context
        scriptStream.write('(')
        scriptStream.write('\n')
        scriptStream.write('set -ex')
        scriptStream.write('\n')

        # Prepare before_script commands
        if len(scriptsBefore) > 0:
            scriptStream.write('{')
            scriptStream.write('\n')
            scriptStream.write('\n'.join(scriptsBefore))
            scriptStream.write('\n')
            scriptStream.write('} && ')
            scriptStream.flush()

        # Prepare script commands
        if len(scriptsCommands) > 0:
            scriptStream.write('{')
            scriptStream.write('\n')
            scriptStream.write('\n'.join(scriptsCommands))
            scriptStream.write('\n')
            scriptStream.write('}')
            scriptStream.flush()
        else:
            scriptStream.write('false')
            scriptStream.flush()

        # Finish before_script/script context
        scriptStream.write('\n')
        scriptStream.write(') 2>&1')
        scriptStream.write('\n')
        scriptStream.write('result=${?}')
        scriptStream.flush()

        # Prepare debug script commands
        if len(scriptsDebug) > 0:
            scriptStream.write('\n')
            scriptStream.write('(')
            scriptStream.write('\n')
            scriptStream.write('set -x')
            scriptStream.write('\n')
            scriptStream.write('\n'.join(scriptsDebug))
            scriptStream.write('\n')
            scriptStream.write(') 2>&1')
            scriptStream.flush()

        # Prepare after_script commands
        if len(scriptsAfter) > 0:
            scriptStream.write('\n')
            scriptStream.write('(')
            scriptStream.write('\n')
            scriptStream.write('set -ex')
            scriptStream.write('\n')
            scriptStream.write('{')
            scriptStream.write('\n')
            scriptStream.write('\n'.join(scriptsAfter))
            scriptStream.write('\n')
            scriptStream.write('}')
            scriptStream.write('\n')
            scriptStream.write(') 2>&1')
            scriptStream.flush()

        # Prepare container result
        if not local_runner:
            scriptStream.write('\n')
            scriptStream.write('echo "%s:${result}"' % (marker_result))

        # Prepare execution result
        scriptStream.write('\n')
        scriptStream.write('exit "${result}"')
        scriptStream.write('\n')

    # Prepare script execution
    script_stat = os.stat(scriptStream.name)
    os.chmod(scriptStream.name, script_stat.st_mode | stat.S_IEXEC)
    scriptFile.file.close()

    # Prepare mounts
    temp_dir = tempfile.gettempdir()
    volumes = {
        pathParent: {
            'bind': pathParent,
            'mode': 'rw'
        },
        temp_dir: {
            'bind': temp_dir,
            'mode': 'rw'
        }
    }

    # Extend mounts
    if options.volume:
        for volume in options.volume:
            volume_nodes = volume.split(':')

            # Parse HOST:TARGET:MODE
            if len(volume_nodes) == 3:
                volume_host = os.path.abspath(os.path.expandvars(volume_nodes[0]))
                volume_target = os.path.expandvars(volume_nodes[1])
                volume_mode = volume_nodes[2]

            # Parse HOST:TARGET
            elif len(volume_nodes) == 2:
                volume_host = os.path.abspath(os.path.expandvars(volume_nodes[0]))
                volume_target = os.path.expandvars(volume_nodes[1])
                volume_mode = 'rw'

            # Parse VOLUME
            else:
                volume_host = os.path.abspath(os.path.expandvars(volume))
                volume_target = os.path.abspath(os.path.expandvars(volume))
                volume_mode = 'rw'

            # Clear volume overrides
            for volume in list(volumes.keys()):
                if volume_target == volumes[volume]['bind']:
                    volumes.pop(volume)

            # Append volume mounts
            volumes[volume_host] = {'bind': volume_target, 'mode': volume_mode}

    # Prepare variables
    variables = dict()
    for variable in job_data['variables']:
        variables[variable] = os.path.expandvars(str(job_data['variables'][variable]))

    # Configure local variables
    variables['CI_LOCAL'] = 'true'

    # Container execution
    if not local_runner:

        # Create container engine
        if engine is None:
            engine = Engine()
            engine.sockets(volumes)

        # Image validation
        if not image:
            raise ValueError(
                'Missing image for "%s / %s"' % (job_data['stage'], job_data['name']))
        engine.get(image)

        # Launch container
        container = engine.run(image, scriptFile.name, entrypoint, variables, network,
                               volumes, pathWorkDir)

        # Create interruption handler
        def interruptHandler(signal, frame):
            print(' ')
            print(' ')
            print(
                ' %s> WARNING: %sUser interruption detected, stopping the container...%s'
                % (colored.fg('yellow') + colored.attr('bold'),
                   colored.attr('reset') + colored.attr('bold'), colored.attr('reset')))
            print(' ', flush=True)
            engine.stop(container, 0)

        # Register interruption handler
        originalINTHandler = signal.getsignal(signal.SIGINT)
        originalTERMHandler = signal.getsignal(signal.SIGTERM)
        signal.signal(signal.SIGINT, interruptHandler)
        signal.signal(signal.SIGTERM, interruptHandler)

        # Execution wrapper
        scriptResult = 1
        success = False

        # Show container logs
        try:
            for line in engine.logs(container):
                if isinstance(line, bytes):
                    line_decoded = line.decode()
                    if marker_debug in line_decoded:
                        break
                    elif marker_result in line_decoded:
                        scriptResult = int(line_decoded.split(':')[-1])
                        break
                    sys.stdout.buffer.write(line)
                    sys.stdout.buffer.flush()
                else:
                    if marker_debug in line:
                        break
                    elif marker_result in line:
                        scriptResult = int(line.split(':')[-1])
                        break
                    sys.stdout.write(line)
                    sys.stdout.flush()
        except:
            pass

        # Runner bash or debug mode
        if options.bash or options.debug:

            # Select shell
            shell = 'sh'
            if engine.supports(image, container, 'bash'):
                shell = 'bash'

            # Acquire container informations
            container_exec = engine.help('exec')
            container_name = engine.name(container)

            # Footer debugging informations
            print(' ')
            print(
                ' %s> INFORMATION: %sUse \'%s%s %s %s%s\' commands for debugging. Interrupt with Ctrl+C...%s'
                % (colored.fg('yellow') + colored.attr('bold'),
                   colored.attr('reset') + colored.attr('bold'),
                   colored.fg('cyan'), container_exec, container_name, shell,
                   colored.attr('reset') + colored.attr('bold'), colored.attr('reset')))
            print(' ', flush=True)

        # Check container status
        success = engine.wait(container, scriptResult)

        # Stop container
        engine.stop(container, 0)
        time.sleep(0.1)

        # Remove container
        engine.remove(container)

        # Unregister interruption handler
        signal.signal(signal.SIGINT, originalINTHandler)
        signal.signal(signal.SIGTERM, originalTERMHandler)

        # Result evaluation
        if job_data['when'] in ['on_failure', 'always']:
            result = last_result
        elif success:
            result = True

    # Native execution
    else:

        # Prepare environment
        _environ = dict(os.environ) # or os.environ.copy()
        os.environ.update(variables)

        # Native execution
        scripts = []
        if entrypoint:
            scripts += entrypoint
        scripts += [scriptFile.name]
        success = (os.system(' '.join(scripts)) == 0)

        # Result evaluation
        if job_data['when'] in ['on_failure', 'always']:
            result = last_result
        elif success:
            result = True

        # Restore environment
        os.environ.clear()
        os.environ.update(_environ)

    # Initial job details
    job_details = ''
    job_details_list = []

    # Prepare when details
    if job_data['when'] not in ['on_success']:
        job_details_list += ['when: %s' % (job_data['when'])]

    # Prepare allow_failure details
    if job_data['allow_failure']:
        job_details_list += ['failure allowed']

    # Prepare job details
    if job_details_list:
        job_details = ' (' + ', '.join(job_details_list) + ')'

    # Evalulate duration time
    time_current = time.time()
    time_duration = time_current - time_start
    time_seconds = '%.0f second%s' % (time_duration % 60,
                                      's' if time_duration % 60 > 1 else '')
    time_minutes = ''
    if time_duration >= 60:
        time_minutes = '%.0f minute%s ' % (time_duration / 60,
                                           's' if time_duration / 60 > 1 else '')
    time_string = time_minutes + time_seconds

    # Evalulate duration total time
    time_total_duration = time_current - time_launcher
    time_total_seconds = '%.0f second%s' % (time_total_duration % 60,
                                            's' if time_total_duration % 60 > 1 else '')
    time_total_minutes = ''
    if time_total_duration >= 60:
        time_total_minutes = '%.0f minute%s ' % (time_total_duration / 60, 's'
                                                 if time_total_duration / 60 > 1 else '')
    if round(time_total_duration, 3) > round(time_duration, 3):
        time_total_string = ' (total of ' + time_total_minutes + time_total_seconds + ')'
    else:
        time_total_string = ''

    # Footer
    print(' ', flush=True)
    if not options.quiet:
        print(' %s> Result: %s in %s%s%s%s%s' %
              (colored.fg('yellow') + colored.attr('bold'), colored.fg('green') +
               colored.attr('bold') + 'Success' if result else colored.fg('red') +
               colored.attr('bold') + 'Failure', time_string, colored.attr('reset') +
               colored.attr('bold'), time_total_string, colored.fg('cyan') +
               colored.attr('bold') + job_details, colored.attr('reset')))
        print(' ')
        print(' ', flush=True)

    # Allowed failure result
    if job_data['when'] not in ['on_failure', 'always'
                                ] and not result and job_data['allow_failure']:
        result = True

    # Result
    return result
