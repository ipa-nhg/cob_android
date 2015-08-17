#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['cob_android_script_server'],
   package_dir={'': 'src'},
   scripts['scripts/script_server_android'],
   requires=['rospkg']
)

setup(**d)
