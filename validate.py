#!/usr/bin/env python3

import json
import os.path as path
import sys

import jsonschema
import jsonschema.exceptions as jsonexceptions

if len(sys.argv) < 2:
    sys.exit("Usage: validate /path/to/config.json")

filepath = path.abspath(sys.argv[1])
if not path.exists(filepath):
    print(f"No such file '{filepath}'")

schema: dict
with open('schema.json', 'r') as fp:
    schema = json.load(fp)

datum: dict
try:
    with open(filepath, 'r') as fp:
        datum = json.load(fp)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)
    sys.exit(-1)

try:
    jsonschema.validate(datum, schema)
except jsonexceptions.ValidationError as e:
    print("Invalid schema:", e)
    sys.exit(-1)
