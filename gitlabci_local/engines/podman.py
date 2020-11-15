#!/usr/bin/env python3

# Libraries
import os
import podman
import stat
import tempfile
import time

# Podman class
class Podman:

    # Members
    client = None

    # Constructor
    def __init__(self):

        # Engine client
        self.client = podman.Client()

    # Exec
    def exec(self, container, command):

        # Execute command in container
        raise NotImplementedError('Unsupported exec command in the Podman engine...')

    # Help
    def help(self, command):

        # Exec command
        if command is 'exec':
            if 'SUDO_USER' in os.environ:
                return 'sudo podman exec -it'
            else:
                return 'podman exec -it'

        # Default fallback
        return ''

    # Get
    def get(self, image):

        # Validate image exists
        try:
            self.client.images.get(image)

        # Pull missing image
        except:
            self.pull(image)

    # Logs
    def logs(self, container):

        # Return logs stream
        return container.logs()

    # Name
    def name(self, container):

        # Result
        return container.stats().name

    # Pull
    def pull(self, image):

        # Header
        print('Pulling from %s' % (image), flush=True)

        # Pull image with logs stream
        id = self.client.images.pull(image)

        # Layer completion logs
        print('Digest: %s' % (id))
        print('Status: Image is up to date for %s' % (image))

        # Footer
        print(' ', flush=True)

    # Remove
    def remove(self, container):

        # Remove container
        container.remove(force=True)

    # Run
    def run(self, image, command, entrypoint, variables, network, volumes, directory):

        # Variables
        mount = []

        # Acquire image
        image = self.client.images.get(image)

        # Adapt entrypoint
        if isinstance(entrypoint, list):
            if len(entrypoint) > 1:
                if isinstance(command, str):
                    command = [command]
                command = [' '.join(command)]
                command[0:0] = entrypoint[1:]
            entrypoint = entrypoint[0]

        # Adapt mounts
        if isinstance(volumes, dict):
            for volume in volumes.items():
                options = ''
                if volume[1]['mode'] == 'ro':
                    options += ',ro=true'
                elif volume[1]['mode'] == 'rw':
                    options += ',rw=true'
                mount += [
                    'type=bind,src=%s,target=%s%s' %
                    (volume[0], volume[1]['bind'], options)
                ]

        # Create container image
        container = image.container(command=command, detach=True, entrypoint=entrypoint,
                                    env=variables, rm=False, tty=True, mount=mount,
                                    securityOpt=['label=disable'], workDir=directory)

        # Start container
        return container.start()

    # Sockets
    def sockets(self, volumes):
        pass

    # Stop
    def stop(self, container, timeout):

        # Stop container
        try:
            container.stop(timeout=timeout)
        except podman.libs.errors.InvalidState:
            pass
        except:
            pass

    # Supports
    def supports(self, image, container, binary):

        # Variables
        exit_code = False
        test = None

        # Prepare commands
        scriptFile = tempfile.NamedTemporaryFile(delete=True)
        with open(scriptFile.name, mode='w') as scriptStream:

            # Prepare execution context
            scriptStream.write('#!/bin/sh')
            scriptStream.write('\n')
            scriptStream.write('whereis %s' % binary)
            scriptStream.write('\n')
            scriptStream.write('result=${?}')
            scriptStream.write('\n')
            scriptStream.write('sleep 1')
            scriptStream.write('\n')
            scriptStream.write('exit "${result}"')
            scriptStream.write('\n')

        # Prepare script execution
        script_stat = os.stat(scriptStream.name)
        os.chmod(scriptStream.name, script_stat.st_mode | stat.S_IEXEC)
        scriptFile.file.close()

        # Prepare mounts
        temp_dir = tempfile.gettempdir()
        volumes = {temp_dir: {'bind': temp_dir, 'mode': 'rw'}}

        # Validate binary support
        try:
            test = self.run(image, scriptFile.name, None, None, 'bridge', volumes, None)
            exit_code = self.wait(test, 1)
        except:
            pass

        # Cleanup test container
        if test:
            self.stop(test, 0)
            time.sleep(0.1)
            self.remove(test)

        # Result
        return exit_code

    # Wait
    def wait(self, container, result):

        # Wait container
        if container.refresh().status != 'exited':
            result = container.wait()

        # Result
        return result == 0
