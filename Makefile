.PHONY: install test sdist testsdist upload clean

install:
	$(MAKE) -C test_framework install

test:
	$(MAKE) -C test_framework test

sdist:
	python setup.py sdist

testsdist: sdist
	pip install dist/factory_djoy-*.tar.gz

upload:
	python setup.py register

clean:
	python setup.py clean
	rm -r dist
	find . -name '*.pyc' -delete
