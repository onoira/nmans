#!/usr/bin/env python3
"""Validate a configuration file against schema.json"""

import json
import os.path as path
import sys
from typing import Any

import jsonschema
import jsonschema.exceptions as jsonexceptions

if len(sys.argv) < 2:
    sys.exit("Usage: validate /path/to/config.json")

filepath = path.abspath(sys.argv[1])
if not path.exists(filepath):
    print(f"No such file '{filepath}'")

schema: dict[Any, Any]
with open('schema.json', 'r') as fp:
    schema = json.load(fp)

datum: dict[Any, Any]
try:
    with open(filepath, 'r') as fp:
        datum = json.load(fp)
except json.JSONDecodeError as ex:
    print("Invalid JSON:", ex)
    sys.exit(-1)

try:
    jsonschema.validate(datum, schema)
except jsonexceptions.ValidationError as ex:
    print("Invalid schema:", ex)
    sys.exit(-1)

print("OK")
