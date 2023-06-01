DOCKER_APP=boilerplate-api
MAKELIB=.makelib
PYTHON_PACKAGE=boilerplate
RELEASE_GIT=git@gitlab.com:gotecq-deploy/api-build/boilerplate-api.git
TARGET_ENV?=boilerplate

CONFIG_FILE:='env/$(TARGET_ENV)/cfg/config.ini'
PYTEST:=FII_APP_CONFIG_FILE=$(CONFIG_FILE) PYTHONPATH=./src:./lib pytest
PYTEST_PARAM?= -q -W ignore::DeprecationWarning --html=tests/logs/report.html --self-contained-html

PYTHON:=FII_APP_CONFIG_FILE=$(CONFIG_FILE) PYTHONPATH=./src:./lib python

include $(MAKELIB)/common.mk
include $(MAKELIB)/docker.mk
include $(MAKELIB)/postgres.mk
include $(MAKELIB)/python.mk

install:
	pip install -r requirements.txt
	pip install -r requirements.dev.txt

run:
	@$(PYTHON) -m boilerplate_api

test-boilerplate:
	@$(PYTEST) $(PYTEST_PARAM) -m debug test/test_boilerplate.py
