#!/usr/bin/env python3

# Libraries
import os

# Puller
def puller(options, jobs):

    # Variables
    images = []
    result = False

    # List Docker images
    for job in jobs:
        image = jobs[job]['image']
        if image and image != 'local' and image not in images:
            images += [image]
            result = True

    # Pull Docker images
    if images:
        images.sort()
        for image in images:
            os.system('docker pull %s' % (image))
            print(' ', flush=True)

    # Result
    return result
