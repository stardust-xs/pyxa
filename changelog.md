<p align="center">
  <a href="https://github.com/xames3/pyxa/blob/master/changelog.md">
    <img alt="pyXA Changelog" title="pyXA Changelog" src="https://github.com/xames3/pyxa/blob/assets/files/github_changelog_banner.png?raw=true">
  </a>
</p>

All notable changes to this project will be documented in this file.<br>
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) starting with version 0.0.1.

## [Unreleased]
### [0.0.3] - 2019-12-06
### Added
- new function `resolve_days` (old one is now `resolve_number_of_days`).

### Changed
- old `resolve_days` function to `resolve_number_of_days`.

## Removed
- unused `os` import.

## [Stable releases]
### [0.0.2] - 2019-12-05
#### Added
- ported important modules like `constants.py`, `dataset.py`, `location.py`, `system.py` and `weather.py` from Charlotte.
- `find_string` function from Charlotte.
- `DEFAULT_WEATHER_URL` for making weather related API calls.

#### Fixed
- linting issues with some files.

## [Alpha release]
### [0.0.2a1] - 2019-11-29

#### Added
- github banner and Table of Contents to the `README.md` file.
- `Why pyXA?`, `Changelog`, `Contributors` and `License` section in the `README.md` file.
- github changelog banner to the `assets` branch.
- `changelog.md` file.
- a new function, `check_version` in `common.py`
- directory and file symlinks to be ignored in `.gitignore`.
- user data in `profile.yml` file.

#### Changed
- version to `0.0.2a1` in `settings.py`.
- `exceptions.py` docstring. Now it elaborately describes what it does.
- docstrings of all the classes under `exceptions.py`.
- `settings.py`, `setup.py`, `parser.py`, `exceptions.py`, `common.py`, `strings.py` docstring. 
- `setup.py` now uses `README.md` file for its long description.
- formatted all scripts with pylint and pyright.
- docstrings for all the scripts.
- `check_version` is now used for displaying the version details.
- `virtualenv` is now `venv` by default for all options and arguments.

#### Fixed
- `AUTHOR_EMAIL` and `MAINTAINER_EMAIL` to correct email.
- `changelog.md` headers.
- year and qwner name in `LICENSE` file.
- `Bad first argument given to super()` warning in `formatter.py`.
- rounded output of `_split_lines` method in `formatter.py`.

#### Removed
- section for `Secret keys` in `settings.py` and boilerplate code for the keys.
- unnecessary comments in `README.md` file.
- `virtualenv` from `requirements.txt` file in favor of `venv`.
- removed '/' from the `.gitignore` file for added files and folders.
- `__future__` imports as the project doesn't support backporting.
- `logger` from `parser.py`.
- `FileNotFound` and `PathNotFound` exception in favor of builtin `FileNotFoundError` and `NotADirectoryError` respectively.
- `user.py` module and creating profile functionality.
- strings associated with `profile` subparser object from `strings.py`.

### [0.0.1rc1] - 2019-11-21

#### Added
- project to this repository.
