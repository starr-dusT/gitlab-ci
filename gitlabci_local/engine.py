#!/usr/bin/env python3

# Libraries
from enum import Enum

# Components
from .engines import docker, podman

# Backend enumeration
class Backend(Enum):
    DOCKER = 1
    PODMAN = 2
    UNKNOWN = 3

# Engine class
class Engine:

    # Members
    backend = Backend.UNKNOWN
    engine = None

    # Constructor
    def __init__(self):

        # Podman engine detection
        if not self.engine:
            try:
                self.engine = podman.Podman()
                self.backend = Backend.PODMAN
            except:
                self.engine = None

        # Docker engine detection
        if not self.engine:
            try:
                self.engine = docker.Docker()
                self.backend = Backend.DOCKER
            except:
                self.engine = None

        # Unknown engine fallback
        if not self.engine:
            raise NotImplementedError('Unknown or unsupported container engine...')

    # Exec
    def exec(self, container, command):
        return self.engine.exec(container, command)

    # Help
    def help(self, command):
        return self.engine.help(command)

    # Get
    def get(self, image):
        self.engine.get(image)

    # Logs
    def logs(self, container):
        return self.engine.logs(container)

    # Name
    def name(self, container):
        return self.engine.name(container)

    # Pull
    def pull(self, image):
        self.engine.pull(image)

    # Remove
    def remove(self, container):
        self.engine.remove(container)

    # Run
    def run(self, image, command, entrypoint, variables, network, volumes, directory):
        return self.engine.run(image, command, entrypoint, variables, network, volumes,
                               directory)

    # Sockets
    def sockets(self, volumes):
        self.engine.sockets(volumes)

    # Stop
    def stop(self, container, timeout):
        self.engine.stop(container, timeout)

    # Supports
    def supports(self, image, container, binary):
        return self.engine.supports(image, container, binary)

    # Wait
    def wait(self, container, result):
        return self.engine.wait(container, result)
