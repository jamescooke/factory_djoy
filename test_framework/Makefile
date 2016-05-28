.PHONY: venv install requirements clean

venv:
	virtualenv venv --python=python3.5
	. venv/bin/activate && pip install pip==8.1.1  # Pin pip to pip-tools required version

install:
	pip install -r requirements/base.txt
	pip install -e ..

requirements:
	$(MAKE) -C requirements

clean:
	find . -name '*.pyc' -delete
