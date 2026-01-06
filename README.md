<!--
SPDX-FileCopyrightText: Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>

SPDX-License-Identifier: MPL-2.0
-->

# pgm-build-dependencies

A proxy Python package to host all header-only libraries which are needed to build Power Grid Model.

The GitHub Actions automatically fetches the latest versions of the header-only libraries and updates the `pgm-build-dependencies` package.

## Installation and Usage

This package should be part of build dependencies of the Power Grid Model project.
Given its limited applicability, we deliberately do not publish it to PyPI, but instead use a GitHub release artifact to store the wheel file.

### As build dependency for Python

```toml
[build-system]
requires = [
    "pgm-build-dependencies@https://github.com/PowerGridModel/pgm-build-dependencies/releases/latest/download/pgm_build_dependencies-0.1.0-py3-none-any.whl",
]
```

In the build process, the entry point `cmake.root` will be installed into the build environment. The build backend, e.g., [`scikit-build-core`](https://github.com/scikit-build/scikit-build-core), can retrieve the `cmake` search paths and use them when invoking `cmake`.

### Load into CI for C++ build

```yaml
    steps:
      - name: Install uv
        uses: astral-sh/setup-uv@v5
      
      - name: Install pgm-build-dependencies
        run: |
          uv tool install https://github.com/PowerGridModel/pgm-build-dependencies/releases/latest/download/pgm_build_dependencies-0.1.0-py3-none-any.whl
          pgm-build-setup-ga-ci
```

After setting this in your GitHub Actions CI, the follow-up `cmake` calls will find the packages.

## License

The source code of this package is licensed under the [MPL-2.0](https://spdx.org/licenses/MPL-2.0.html) license.

The header-only libraries are licensed under their respective licenses, which can be found in the [`LICENSES`](LICENSES) directory of this package.
