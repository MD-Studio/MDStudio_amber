#!/bin/bash

export MD_CONFIG_ENVIRONMENTS=dev,docker

# Source AmberTools either pre-installed or Conda installed
if [[ $AMBERHOME ]]; then
    source ${AMBERHOME}/amber.sh
    echo "Existing AmberTools installation found at: ${AMBERHOME}"
elif [[ -f /usr/local/amber.sh ]]; then
    source /usr/local/amber.sh
    echo "Use conda AmberTools installation at: ${AMBERHOME}"
else
    echo "ERROR: no AmberTools installation found" >&2
    exit
fi

python -u -m mdstudio_amber
