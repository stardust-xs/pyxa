# Copyright 2019 XAMES3. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ======================================================================
"""
The :mod:`pyxa.utils.exceptions` module includes all custom warnings and
error classes used across pyXA.
"""


class PyXAException(Exception):
    """Exception class to raise errors by pyXA module.

    This class inherits base exception to help with the exception
    handling and backward compatibility.
    """
    pass


class FileNotFound(PyXAException, FileNotFoundError):
    """Exception class to raise if the file in path is not found.

    This class inherits from both PyXAException and FileNotFoundError
    and occurs when the file mentioned by the user is not found in the
    said directory.

    For example, this exception may occur when the user
        - tries to access file from `X` directory and the file doesn't
          exists.
        - tries to access file from `X` directory and the user makes a
          typo while specifying the file name.
    """
    pass


class PathNotFound(PyXAException, FileNotFoundError):
    """Exception class to raise if the path provided by the user is not
    found.

    This class inherits from both PyXAException and FileNotFoundError
    and occurs when the path mentioned by the user is not found.

    For example, this exception may occur when the user
        - tries to access path in some directory but the path specified
          is incorrect.
        - tries to access path in some directory before it is mentioned
          for it's existence.
    """
    pass
