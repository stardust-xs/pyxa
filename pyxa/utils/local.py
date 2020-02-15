# Copyright 2020 XAMES3. All Rights Reserved.
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
The `pyxa.utils.local` module implements the local file operations.

These are local simple file operations.
"""

import os
import shutil
from pathlib import Path
from typing import Optional


def create_dir_with_same_filename(file: str) -> str:
  """Create directory with same filename and return its path.

  Args:
    file: File to be used for creating directory.

  Returns:
    Directory path.
  """
  directory_path = os.path.join(os.path.dirname(file), Path(file).stem)
  if not os.path.isdir(directory_path):
    os.mkdir(directory_path)
  return directory_path


def create_copy(file: str,
                copy_path: Optional[str] = None,
                copy_name: Optional[str] = None) -> str:
  """Create copy of the file and return path of the copied file.

  Args:
    file: File to be copied.
    copy_path: Path (default: None) where the copy needs to be created.
    copy_name: Name (default: None) of the copy file.

  Returns:
    Path where the copy is created.
  """
  if copy_path is None:
    copy_path = create_dir_with_same_filename(file)
  if copy_name is None:
    copy_name = os.path.basename(file)
  return shutil.copy(file, os.path.join(copy_path, copy_name))


def temporary_rename(file: str, rename: Optional[str] = 'temp_xa') -> str:
  """Renames file temporarily for operation."""
  temp_name = os.path.splitext(file)
  return ''.join([temp_name[0], rename, temp_name[1]])


def temporary_copy(file: str) -> str:
  """Creates a temporary copy for operation."""
  temp_file = temporary_rename(file)
  return shutil.copy(file, temp_file)
