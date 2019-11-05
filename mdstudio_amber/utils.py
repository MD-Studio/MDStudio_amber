# -*- coding: utf-8 -*-

import os


def get_amber_config(request):
    """
    Remove the keywords not related to amber
    """
    d = request.copy()
    keys = ['workdir', 'structure']

    for k in keys:
        if k in d:
            d.pop(k)

    return d


def call_amber_package(request, config, function):
    """
    Create temporary files and invoke the `function` using `config`.
    """

    # Create unique workdir and save file
    workdir = request['workdir']
    if not os.path.isdir(workdir):
        os.mkdir(workdir)

    tmp_file = os.path.join(workdir, 'input.{0}'.format(request['structure'].get('extension', 'mol2')))
    with open(tmp_file, 'w') as inp:
        inp.write(request['structure']['content'])

    # Run amber function
    output = function(tmp_file, config, workdir)
    return output


def encoder(file_path):
    """
    Encode the content of `file_path` into a simple dict.
    """
    extension = os.path.splitext(file_path)[1]
    with open(file_path, 'r') as f:
        content = f.read()

    return {"path": file_path, "extension": extension.lstrip('.'),
            "content": content, "encoding": "utf8"}


def encode_file(val):
    if not os.path.isfile(val):
        return val
    else:
        return encoder(val)