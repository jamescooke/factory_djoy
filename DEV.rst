Development
===========

How to work on Factory Djoy.


Build environment and install
-----------------------------

This project is structured with a test framework available in the
``test_framework`` folder. The goal of this is to facilitate testing with
different versions of Django. Each version of Django will have its own module
in ``test_framework`` with models available. Tox is used to manage versions of
Python and Django.

Clone the repository::

    git clone git@github.com:jamescooke/factory_djoy.git

Create a virtual environment. This uses a bare call to ``virtualenv``, you
might prefer to use ``workon``::

    make venv

Activate the virtual environment and install requirements::

    . venv/bin/activate
    make install

Run all tests using ``tox`` for all versions of Python and Django::

    make test

Circle will also run linting before the main test run::

    make lint


Helpers
-------

The ``Makefile`` has a couple of helper recipes:

* ``sdist``: Creates the distribution.
* ``register``: Use ``twine`` to register with PyPI.
* ``upload``: Push generated distribution to PyPI.
* ``clean``: Remove all compiled Python files, distributions, etc.
