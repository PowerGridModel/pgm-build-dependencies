# SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

from importlib.metadata import entry_points
import os

def cmake_prefix_path():
    """Output a single CMAKE_PREFIX_PATH usable for CMake (common parent of all cmake.root packages).
    """
    cmake_roots = entry_points(group="cmake.root")

    paths = []
    for ep in cmake_roots:
        loaded = ep.load()
        paths.append(loaded.__path__[0])

    if paths:
        common_path = os.path.commonpath(paths)
        print(common_path)
    else:
        print("")
