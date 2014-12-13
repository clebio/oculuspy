#! /usr/bin/env python
'''
Python bindings for Oculus Rift, based on [1]

[1]: http://pybindgen.readthedocs.org/en/latest/tutorial/#header-file-scanning-with-py-gccxml
'''


import sys
import os
import logging

from pybindgen import FileCodeSink, write_preamble
from pybindgen.gccxmlparser import ModuleParser

logging.basicConfig(filename='ovr.log', level=logging.WARN)

base_dir = sys.argv[1]
build_dir = 'output'

if not os.path.exists(build_dir):
    os.mkdir(build_dir)

def my_module_gen():
    include_paths = [base_dir + '/Include', base_dir + '/Src']
    header_files = []

    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith('.h'):
                header_files.append(root + '/' + filename)

    module_parser = ModuleParser('OVR', '::')

    modules = dict()

    for header in header_files:

        name = header.split('/').pop()
        name = name.split('.')[0]
        try:
            modules[name] = module_parser.parse(
                [header, ],
                gccxml_options = dict(include_paths=include_paths),
                )
        except Exception as _ex:
            logging.warning(
                "Couldn't parse {}: {}\n".format(header, _ex.message)
                )

    for name, module in modules.iteritems():
        try:
            outfile = open(build_dir + '/' + name + '.c', 'w')
            write_preamble(FileCodeSink(outfile))
            module.generate(FileCodeSink(outfile))
            if not outfile.closed:
                outfile.close()
        except Exception as _ex:
            logging.warning(
                "Couldn't write {}: {}\n".format(name, _ex.message)
                )

if __name__ == '__main__':
    my_module_gen()
