.PHONY: venv install test lint sdist upload requirements clean

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

sdist:
	python setup.py sdist

upload:
	twine upload dist/factory_djoy-*.tar.gz

requirements:
	$(MAKE) -C requirements

clean:
	python setup.py clean
	-rm -r dist
	-rm -r .tox
	find . -name '*.pyc' -delete
