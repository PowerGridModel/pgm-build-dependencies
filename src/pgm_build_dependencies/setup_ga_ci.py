# SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

from importlib.metadata import entry_points
import os


def setup_ga_ci():
    """Setup CI environment for GitHub Actions"""
    # Get all cmake.root entry points from installed packages
    cmake_roots = entry_points(group="cmake.root")

    # Build paths dictionary from entry points
    paths = {}
    for ep in cmake_roots:
        loaded = ep.load()
        paths[f"{ep.name}_DIR"] = loaded.__path__[0]
    github_env = os.getenv("GITHUB_ENV")
    if github_env:
        with open(github_env, "a") as env_file:
            for key, value in paths.items():
                env_file.write(f"{key}={value}\n")
    else:
        # Fallback for local testing
        for key, value in paths.items():
            print(f"{key}={value}")
