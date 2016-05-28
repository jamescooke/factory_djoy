.PHONY: install test sdist testsdist

install:
	$(MAKE) -C test_framework install

test:
	$(MAKE) -C test_framework test

sdist:
	python setup.py sdist

testsdist: sdist
	pip install dist/factory_djoy-*.tar.gz
