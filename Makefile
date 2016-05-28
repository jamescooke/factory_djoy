.PHONY: venv install test lint sdist upload requirements clean

venv:
	virtualenv venv --python=python3.5
	. venv/bin/activate && pip install pip==8.1.1  # Pin pip to pip-tools required version

install:
	pip install -r requirements/base.txt

test:
	tox

lint:
	flake8 factory_djoy

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
