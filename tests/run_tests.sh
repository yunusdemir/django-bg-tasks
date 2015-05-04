#!/bin/sh

TESTS_DIR=$(dirname $0)
export PYTHONPATH=$TESTS_DIR/..:$TESTS_DIR

python `which django-admin.py` test background_task --settings=test_settings
