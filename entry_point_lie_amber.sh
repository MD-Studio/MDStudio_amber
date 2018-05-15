#!/bin/bash

export MD_CONFIG_ENVIRONMENTS=dev,docker

# Load amber
. /home/mdstudio/amber18/amber.sh

python -u -m lie_amber
