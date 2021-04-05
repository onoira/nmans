#!/usr/bin/env sh
coverage run --omit='**/site-packages/*,tests/*' -m unittest discover -v tests/
coverage report -m