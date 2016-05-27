.PHONY: venv install install-dev test flake8 requirements clean

venv:
	virtualenv venv --python=python3
	. venv/bin/activate && pip install pip==8.1.1  # Pin pip to pip-tools required version

install:
	pip install -r requirements/base.txt
	pip install -r requirements/django-1.9.txt
	pip install -e ..

install-dev: install
	pip install -r requirements/dev.txt

test:
	cd django_1_9 && ./manage.py test

flake8:
	flake8 ../factory_djoy

requirements:
	+$(MAKE) -C requirements all

clean:
	rm -rf venv
