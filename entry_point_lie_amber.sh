#!/bin/bash

export MD_CONFIG_ENVIRONMENTS=dev,docker
cd $HOME/lie_amber

python -u -m lie_amber
