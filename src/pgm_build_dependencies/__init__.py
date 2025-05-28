# SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

from pathlib import Path

from importlib_resources import files


def get_include() -> Path:
    return files("pgm_build_dependencies.include")


def print_include() -> None:
    print(get_include(), end="")
