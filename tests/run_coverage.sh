#!/bin/sh

TESTS_DIR=$(dirname $0)
export PYTHONPATH=$TESTS_DIR/..:$TESTS_DIR

echo "=============================== Testing Python2 ==============================="
python2 `which django-admin.py` test_coverage background_task --settings=test_settings

echo "=============================== Testing Python3 ==============================="
python3 `which django-admin.py` test_coverage background_task --settings=test_settings