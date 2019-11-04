# MDStudio_amber

[![Build Status](https://travis-ci.org/MD-Studio/MDStudio_amber.svg?branch=master)](https://travis-ci.org/MD-Studio/MDStudio_amber)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/598ded81ce614380a02d25c3b5992e1b)](https://www.codacy.com/manual/marcvdijk/MDStudio_amber?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MD-Studio/MDStudio_amber&amp;utm_campaign=Badge_Grade)
[![Docker Build Status](https://img.shields.io/docker/build/mdstudio/mdstudio_amber.svg)](https://hub.docker.com/r/mdstudio/mdstudio_amber/)

The MDStudio Amber services offers a [MDStudio](https://github.com/MD-Studio/MDStudio) WAMP API to the functionality of
the [Ambertools](http://ambermd.org/GetAmber.php) software package and the small molecule topology generation services 
powered by the ACPYPE (AnteChamber PYthon Parser interfacE).

## Installation Quickstart
MDStudio Amber can be used in the MDStudio environment as Docker container or as standalone service.

### Install option 1. Pre-compiled Docker container
MDStudio Amber can be installed quickly from a pre-compiled docker image hosted on DockerHub by:

    docker pull mdstudio/mdstudio_amber
    docker run (-d) mdstudio/mdstudio_amber

In this mode you will first need to launch the MDStudio environment itself in order for the MDStudio Amber service to 
connect to it. You can unify this behaviour by adding the MDStudio Amber service to the MDStudio service environment as:

    MDStudio/docker-compose.yml:
        
        services:
           mdstudio_amber:
              image: mdstudio/mdstudio_amber
              links:
                - crossbar
              environment:
                - CROSSBAR_HOST=crossbar
              volumes:
                - ${WORKDIR}/mdstudio_amber:/tmp/mdstudio/mdstudio_mber

And optionally add `mdstudio_amber` to MDStudio/core/auth/settings.dev.yml for automatic authentication and 
authorization at startup.

### Install option 2. custom build Docker container
You can custom build the MDStudio Amber Docker container by cloning the MDStudio_amber GitHub repository and run:

    docker build --build-arg AMBER_TOOLS_VERSION=19 MDStudio_amber/ -t mdstudio/mdstudio_amber
    
The `AMBER_TOOLS_VERSION` build argument is optional and allows you to choose a different AmberTools version to be 
installed other then the default version 19.
After successful build of the container follow the steps starting from `docker run` in install option 1.

### Install option 3. standalone deployment of the service.
If you prefer a custom installation over a (pre-)build docker container you can clone the MDStudio_amber GitHub
repository and install `mdstudio_amber` locally as:

    pip install (-e) mdstudio_amber/
    
This install requires the AmberTools package to be installed and accessible in your environment using the `AMBERHOME`
environment variable. The `acpype` script used by the `mdstudio_amber` package requires the OpenBabel package.
After installation ensure that the `AMBERHOME` environment variable is set and start the service by:

    ./entry_point_mdstudio_amber.sh
    
or

    export MD_CONFIG_ENVIRONMENTS=dev,docker
    python -u -m mdstudio_amber

