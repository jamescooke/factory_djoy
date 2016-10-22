.PHONY: venv install test lint dist upload requirements clean

venv:
	virtualenv venv --python=python3.5
	. venv/bin/activate && pip install -U pip

install:
	pip install -r requirements/base.txt

test:
	tox

lint:
	flake8 factory_djoy
	flake8 tests
	bandit -r factory_djoy

dist:
	python setup.py sdist bdist_wheel

test-upload:
	twine upload -r test dist/factory_djoy-*

test-install:
	pip install -r test_framework/requirements/local.txt
	pip install -i https://testpypi.python.org/pypi factory-djoy

upload:
	twine upload dist/factory_djoy-*

requirements:
	$(MAKE) -C requirements

clean:
	python setup.py clean
	-rm -r build
	-rm -r dist
	-rm -r .tox
	find . -name '*.pyc' -delete
