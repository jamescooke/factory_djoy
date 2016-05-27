venv:
	virtualenv venv --python=python3

requirements-compile:
	pip-compile -v --output-file requirements/base.txt requirements/base.in
	pip-compile -v --output-file requirements/django-1.9.txt requirements/django-1.9.in

requirements:
	pip install -r requirements/django-1.9.txt
	pip install -e ..

test:
	cd django_1_9 && ./manage.py test
