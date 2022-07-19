#!/usr/bin/python3
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import atheris
import sys

with atheris.instrument_imports():
  import xlrd
  import zipfile


def TestOneInput(data):
  temp_file = "myfile.xls"
  with open(temp_file, "wb") as fd:
    fd.write(data)

  try:
    xlrd.open_workbook("myfile.xls")
  except (
    xlrd.XLRDError,
    xlrd.compdoc.CompDocError,
    zipfile.BadZipFile,
    OSError
  ) as e:
    pass


def main():
  atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
  atheris.Fuzz()


if __name__ == "__main__":
  main()
