.PHONY: install test sdist testsdist upload clean

install:
	pip install -r requirements/base.txt

test:
	tox

sdist:
	python setup.py sdist

testsdist: sdist
	pip install dist/factory_djoy-*.tar.gz

register:
	twine register

upload:
	twine upload dist/factory_djoy-*.tar.gz

clean:
	python setup.py clean
	-rm -r dist
	-rm -r .tox
	find . -name '*.pyc' -delete
