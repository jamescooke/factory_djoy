.PHONY: install test lint sdist register upload clean

install:
	pip install -r requirements/base.txt

test:
	tox

lint:
	flake8 factory_djoy

sdist:
	python setup.py sdist

register:
	twine register

upload:
	twine upload dist/factory_djoy-*.tar.gz

clean:
	python setup.py clean
	-rm -r dist
	-rm -r .tox
	find . -name '*.pyc' -delete
