# SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

from importlib.metadata import entry_points
import os

def cmake_prefix_path():
    """Output CMAKE_PREFIX_PATH for all pgm build dependencies"""
    cmake_roots = entry_points(group="cmake.root")
    
    paths = []
    for ep in cmake_roots:
        loaded = ep.load()
        paths.append(loaded.__path__[0])
    
    print(os.pathsep.join(paths))
