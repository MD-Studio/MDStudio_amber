# -*- coding: utf-8 -*-

import json
import os
import pkgutil
import shutil
import tempfile
import unittest

from mdstudio_amber.utils import get_amber_config
from mdstudio_amber.ambertools import amber_acpype


def schema_to_data(schema, data=None, defdict=None):
    """
    Translate the schema for gromacs to an standard python
    dictionary
    """
    default_data = defdict or {}

    properties = schema.get('properties', {})
    for key, value in properties.items():
        if 'properties' in value:
            default_data[key] = schema_to_data(value)
        elif 'default' in value:
            default_data[key] = value.get('default')

    # Update with existing data
    if data:
        default_data.update(data)

    return default_data


ACPYPE_LIE_SCHEMA = os.path.join(
    pkgutil.get_data(
        'mdstudio_amber', 'schemas/endpoints/acpype_request.v1.json'))

settings_acpype = get_amber_config(
    schema_to_data(json.loads(ACPYPE_LIE_SCHEMA)))


class Test_amber_components(unittest.TestCase):

    def setUp(self):
        self.workdir = tempfile.mkdtemp('tmp', dir='.')

    def tearDown(self):
        if self.workdir and os.path.exists(self.workdir):
            shutil.rmtree(self.workdir)

    def test_amber_acepype(self):
        path = os.path.join(os.path.dirname(__file__), '../files/input.mol2')
        shutil.copy(path, self.workdir)
        output = amber_acpype('input.mol2', settings_acpype, self.workdir,
                              acepype_exe=os.path.join(os.path.dirname(__file__), '../../scripts/acpype.py'))
        self.assertTrue(os.path.isdir(output['path']))

    def test_amber_reduce(self):
        pass
