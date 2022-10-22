.PHONY: install
install:
	pip install tox twine

.PHONY: test
test:
	tox -p auto

.PHONY: dist
dist:
	python setup.py sdist bdist_wheel

.PHONY: dist-check
dist-check: dist
	twine check --strict dist/factory_djoy-*

.PHONY: test-upload
test-upload: dist-check
	twine upload --repository-url https://test.pypi.org/legacy/ dist/factory_djoy-*

# Need to manually install dependencies since they are not on test pypi
.PHONY: test-install
test-install:
	pip install Django factory-boy
	pip install factory-djoy -i https://test.pypi.org/simple

.PHONY: upload
upload: dist-check
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/factory_djoy-*

.PHONY: requirements
requirements:
	$(MAKE) -C requirements

.PHONY: clean
clean:
	python setup.py clean
	-rm -r build
	-rm -r dist
	-rm -r .tox
	find . -name '*.pyc' -delete
