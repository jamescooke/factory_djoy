lint_files=setup.py factory_djoy tests

.PHONY: venv
venv:
	virtualenv venv --python=python3
	. venv/bin/activate && pip install -U pip

.PHONY: install
install:
	pip install -r requirements/base.txt

.PHONY: install2
install2:
	pip install -r requirements/base2.txt

.PHONY: test
test:
	tox

.PHONY: lint
lint: flake8 isort dist-check
	bandit -r factory_djoy

.PHONY: flake8
flake8:
	flake8 $(lint_files)

.PHONY: isort
isort:
	isort --check --diff $(lint_files)

.PHONY: fixlint
fixlint:
	@echo "=== fixing isort ==="
	isort --quiet --recursive $(lint_files)

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

.PHONY: on_master
on_master:
	./on_master.sh

.PHONY: bump_reqs
bump_reqs: on_master
	git checkout -b auto/bump-requirements
	rm -f requirements/base.txt
	$(MAKE) -C requirements
	rm test_framework/requirements/*.txt
	cd test_framework && $(MAKE) -C requirements
	git commit requirements/*.txt test_framework/requirements/*.txt \
	    -m "Update requirements with $$(python --version)"
	git push origin auto/bump-requirements
