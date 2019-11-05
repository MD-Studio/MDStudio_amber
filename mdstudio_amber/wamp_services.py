# -*- coding: utf-8 -*-

import os
import shutil

from tempfile import mktemp
from mdstudio.api.endpoint import endpoint
from mdstudio.component.session import ComponentSession

from mdstudio_amber.utils import get_amber_config, call_amber_package, encode_file
from mdstudio_amber.ambertools import amber_acpype, amber_reduce


class AmberWampApi(ComponentSession):
    """
    AmberTools WAMP methods.
    """
    def authorize_request(self, uri, claims):
        return True

    @endpoint('acpype', 'acpype_request', 'acpype_response')
    def run_amber_acpype(self, request, claims):
        """
        Call amber acpype package using a molecular `structure`.
        See the `schemas/endpoints/acpype_request.v1.json for
        details.
        """

        # Load ACPYPE configuration and update
        acpype_config = get_amber_config(request)

        # Create unique workdir name
        workdir = os.path.join(os.path.abspath(request['workdir']), os.path.basename(mktemp()))
        self.log.info('Set ACPYPE workdir to: {0}'.format(workdir))
        self.log.info('Amber installation: {0}'.format(os.environ.get('AMBERHOME')))
        request['workdir'] = workdir

        # Run acpype
        result_files = call_amber_package(request, acpype_config, amber_acpype)

        result = {'status': 'failed', 'output': None}
        if result_files:
            result['output'] = {key: encode_file(val) for key, val in result_files.items()}
            if len(result['output']):
                result['status'] = 'completed'

        # Remove workdir
        shutil.rmtree(workdir)

        return result

    @endpoint('reduce', 'reduce_request', 'reduce_response')
    def run_amber_reduce(self, request, claims):
        """
        Call amber reduce using a  a molecular `structure`.
        See the the `schemas/endpoints/reduce_request.v1.json for
        details.
        """

        reduce_config = get_amber_config(request)

        # Create unique workdir name
        workdir = os.path.join(os.path.abspath(request['workdir']), os.path.basename(mktemp()))
        self.log.info('Set AMBER reduce workdir to: {0}'.format(workdir))
        self.log.info('Amber installation: {0}'.format(os.environ.get('AMBERHOME')))
        request['workdir'] = workdir

        # Run AMBER reduce
        result_files = call_amber_package(request, reduce_config, amber_reduce)

        result = {'status': 'failed', 'output': None}
        if result_files:
            result['output'] = {key: encode_file(val) for key, val in result_files.items()}
            if len(result['output']):
                result['status'] = 'completed'

        # Remove workdir
        shutil.rmtree(workdir)

        return result
