django_version = $(shell python current_django.py)
project_folder = $(django_version)/djoyproject
app_folder = $(django_version)/djoyapp

.PHONY: venv
venv:
	virtualenv venv --python=python3
	. venv/bin/activate && pip install -U pip

.PHONY: install
install:
	pip install -r requirements/django21.txt
	pip install -r requirements/local.txt
	pip install -e ..

.PHONY: build
build: build-project build-app link-models link-tests

.PHONY: build-project
build-project:
	mkdir $(django_version)
	django-admin startproject djoyproject $(django_version)
	cd $(project_folder) && ln -s ../../test_settings.py

.PHONY: build-app
build-app:
	mkdir -p $(app_folder)
	django-admin startapp djoyapp $(django_version)/djoyapp

.PHONY: link-models
link-models:
	rm $(app_folder)/models.py
	cd $(app_folder) && ln -s ../../models.py
	cd $(django_version) && python manage.py makemigrations --settings=djoyproject.test_settings

.PHONY: link-tests
link-tests:
	cd $(django_version) && ln -s ../../tests/

.PHONY: test
test:
	cd $(django_version) && python manage.py test --settings=djoyproject.test_settings

.PHONY: requirements
requirements:
	$(MAKE) -C requirements

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	rm -r $(django_version)
