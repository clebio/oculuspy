#!/usr/bin/env python
import os
from distutils.core import setup, Extension

build_dir = 'output'
sources = []
for root, dirs, files in os.walk(build_dir):
    for filename in files:
        sources.append(build_dir + '/' + filename)

oculus = Extension('oculus',
                     sources = sources,
                     include_dirs=['ovr_sdk_linux_0.4.4/LibOVR/Include', ])

setup(name='OculusPy',
      version="0.1",
      description='Oculus bindings for Python',
      author='Caleb Hyde',
      author_email='caleb.hyde@gmail.com',
      ext_modules=[oculus],
     )
