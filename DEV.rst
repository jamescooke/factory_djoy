Development
===========

How to work on Factory Djoy.

Build environment and install
-----------------------------

This project is structured with a test framework available in the
``test_framework`` folder. The goal of this is to facilitate testing with
different versions of Django.

Clone the repository::

    git clone git@github.com:jamescooke/factory_djoy.git

All work happens from the ``test_framework`` folder::

    cd factory_djoy/test_framework

Using Django 1.9 and the default version of Python 3 on your system. (This uses
a bare call to ``virtualenv``, you might prefer to use ``workon``.)::

    make venv

Activate the virtual environment and install requirements::

    . venv/bin/activate
    make install

Run all tests::

    make test

Update requirements
-------------------

There are multiple requirements files kept in ``test_framework/requirements/``
folder.

On change, they can all be built with ``make``::

    make requirements
