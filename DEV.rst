Development and Testing
=======================

How to work on and test Factory Djoy, across different versions of Django.

Quick start
-----------

The test framework is already in place and ``tox`` is configured to make use of
it. Therefore the quickest way to get going is to make use of it.

Clone the repository and drop in::

    git clone git@github.com:jamescooke/factory_djoy.git
    cd factory_djoy

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


Testing with real Django projects
---------------------------------

``factory_djoy`` is asserted to work with different vanilla versions of Django.
For each version of Django tested, a default project and app exist in the
``test_framework`` folder.

This structure has the following features:

* A folder for each version of Django. For example, the Django 1.9 project is
  in the ``test_framework/django19`` folder. Each project is created with the
  default ``django-admin startproject`` command.

* A test settings file which includes all the default settings as installed by
  Django, but adds the ``djoyapp`` app to the list of ``INSTALLED_APPS``.

* A ``models.py`` installed in the app which provides some models used for
  testing.

* Initial migrations for the models above also exist, created using the
  matching version of Django using the default ``./manage.py makemigrations``
  command.

* A ``tests`` folder wired into the Django project root. These are the tests
  that assert that ``factory_djoy`` behaves as expected.

* Tests are executed through the default ``./manage.py test`` command.

Versioning notes
................

* ``tox`` is used to manage versions of Python and Django installed at test
  time.
* The latest point release from each major Django version is used, excluding
  versions that are no longer supported.
* The current version of Django in use at testing is compiled into each
  ``django*.txt`` file using ``pip-compile`` invoked by ``make requirements``
  in the ``test_framework`` folder.

Creating Django test projects
.............................

Recipes in the test framework's ``Makefile`` sniff out the virtual
environment's currently installed version of Django and use that to create a
test Django project for that version.

To invoke project creation call::

    make build

This creates a new test Django project called ``djoyproject`` containing a
single test app called ``djoyapp``. Then the structures outlined above are
linked and migrations created.


Please note that creating a Django test project will fail if the target folder
already exists. All ``django*`` folders can be removed with ``make clean``.


Working locally
---------------

If there are multiple tests to run this can become inefficient with ``tox``.
Therefore, you can use the helper local environment configured inside
``test_framework``. This installs Python 3.5 and latest Django.

Create a virtual environment and install the requirements::

    cd test_framework
    make venv
    . venv/bin/activate
    make install

The test framework means that all the tests can be run on the test models and
factories using the standard ``manage.py`` test command. So, if working with
Django 1.9, after calling ``make build``::

    cd django19
    ./manage.py test --settings=djoyproject.test_settings


Helper recipes
--------------

The root ``Makefile`` has a couple of helper recipes (note this is different to
the ``Makefile`` in ``test_settings``):

* ``sdist``: Creates the distribution.
* ``upload``: Push generated distribution to PyPI.
* ``requirements``: User ``pip-compile`` to compile all requirements.
* ``clean``: Remove all compiled Python files, distributions, etc.
