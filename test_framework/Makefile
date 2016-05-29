.PHONY: venv install build build-project build-app link-models link-tests test requirements clean

django_version = $(shell python current_django.py)
project_folder = $(django_version)/djoyproject
app_folder = $(django_version)/djoyapp

venv:
	virtualenv venv --python=python3.5
	. venv/bin/activate && pip install pip==8.1.1  # Pin pip to pip-tools required version

install:
	pip install -r requirements/django19.txt
	pip install -r requirements/base.txt
	pip install -e ..

build: build-project build-app link-models link-tests

build-project:
	mkdir $(django_version)
	django-admin startproject djoyproject $(django_version)
	cd $(project_folder) && ln -s ../../test_settings.py

build-app:
	mkdir -p $(app_folder)
	django-admin startapp djoyapp $(django_version)/djoyapp

link-models:
	rm $(app_folder)/models.py
	cd $(app_folder) && ln -s ../../models.py
	cd $(django_version) && python manage.py makemigrations --settings=djoyproject.test_settings

link-tests:
	cd $(django_version) && ln -s ../../tests/

test:
	cd $(django_version) && python manage.py test --settings=djoyproject.test_settings

requirements:
	$(MAKE) -C requirements

clean:
	find . -name '*.pyc' -delete
	rm -r $(django_version)
