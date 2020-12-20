#!/usr/bin/env python3

# Modules libraries
from docker import from_env
from docker.errors import DockerException, ImageNotFound

# Components
from ..system.platform import Platform

# Docker class
class Docker:

    # Members
    __client = None

    # Constructor
    def __init__(self):

        # Engine client
        try:
            self.__client = from_env()
            self.__client.ping()
        except DockerException:
            raise ModuleNotFoundError() from None

    # Command exec
    def cmd_exec(self):

        # Result
        return 'docker exec -it'

    # Exec
    def exec(self, container, command):

        # Execute command in container
        return container.exec_run(command)

    # Get
    def get(self, image):

        # Validate image exists
        try:
            self.__client.images.get(image)

        # Pull missing image
        except ImageNotFound:
            self.pull(image)

    # Logs
    def logs(self, container):

        # Return logs stream
        return container.logs(stream=True)

    # Name
    def name(self, container):

        # Result
        return container.name

    # Pull
    def pull(self, image, force=False):

        # Force image removal
        if force:
            self.rmi(image)

        # Pull image with logs stream
        for data in self.__client.api.pull(image, stream=True, decode=True):

            # Layer progress logs
            if 'progress' in data:
                if Platform.IS_TTY_STDOUT:
                    print(
                        '\r\033[K%s: %s %s' %
                        (data['id'], data['status'], data['progress']), end='')
                    Platform.flush()

            # Layer event logs
            elif 'progressDetail' in data:
                if Platform.IS_TTY_STDOUT:
                    print('\r\033[K%s: %s' % (data['id'], data['status']), end='')
                    Platform.flush()

            # Layer completion logs
            elif 'id' in data:
                print('\r\033[K%s: %s' % (data['id'], data['status']))
                Platform.flush()

            # Image logs
            else:
                print('\r\033[K%s' % (data['status']))
                Platform.flush()

        # Footer
        print(' ')
        Platform.flush()

    # Remove
    def remove(self, container):

        # Remove container
        container.remove(force=True)

    # Remove image
    def rmi(self, image):

        # Remove image
        try:
            self.__client.api.remove_image(image)
        except ImageNotFound:
            pass

    # Run
    def run(self, image, command, entrypoint, variables, network, volumes, directory):

        # Run container image
        return self.__client.containers.run(
            image, command=command, detach=True, entrypoint=entrypoint,
            environment=variables, network_mode=network, privileged=True, remove=False,
            stdout=True, stderr=True, stream=True, volumes=volumes.get(),
            working_dir=directory)

    # Sockets
    def sockets(self, volumes):

        # Add socket volume
        if Platform.IS_LINUX:
            volumes.add('/var/run/docker.sock', '/var/run/docker.sock', 'rw', True)

    # Stop
    def stop(self, container, timeout):

        # Stop container
        container.stop(timeout=timeout)

    # Supports
    def supports(self, container, binary):

        # Validate binary support
        exit_code, unused_output = self.exec(container, 'whereis %s' % (binary))

        # Result
        return exit_code == 0

    # Wait
    def wait(self, container):

        # Wait container
        result = container.wait()

        # Result
        return result['StatusCode'] == 0
