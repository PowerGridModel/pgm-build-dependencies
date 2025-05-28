<!--
SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>

SPDX-License-Identifier: MPL-2.0
-->

# pgm-build-dependencies
A proxy Python package to host all header-only libraries which are needed to build Power Grid Model.

## Installation and Usage

This package should be part of build dependencies of the Power Grid Model project.

```toml
[build-system]
requires = [
    "git+https://github.com/PowerGridModel/pgm-build-dependencies.git",
]
```

## License

The source code of this package is licensed under the [MPL-2.0](https://spdx.org/licenses/MPL-2.0.html) license.

The header-only libraries are licensed under their respective licenses, which can be found in the [`LICENSES`](LICENSES) directory of this package.
