
.. image:: https://img.shields.io/github/workflow/status/jamescooke/factory_djoy/Build
    :alt: GitHub Workflow Status
    :target: https://github.com/jamescooke/factory_djoy/actions?query=branch%3Amaster

.. image:: https://img.shields.io/readthedocs/factory-djoy.svg
    :alt: Read the Docs
    :target: https://factory-djoy.readthedocs.io/

.. image:: https://img.shields.io/pypi/v/factory-djoy.svg
    :alt: PyPI version
    :target: https://pypi.org/project/factory-djoy/

.. image:: https://img.shields.io/pypi/pyversions/factory-djoy.svg
    :alt: Python version
    :target: https://pypi.org/project/factory-djoy/

.. image:: https://img.shields.io/pypi/djversions/factory-djoy
    :alt: PyPI - Django Version
    :target: https://pypi.org/project/factory-djoy/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: factory-djoy is licensed under the MIT License
    :target: https://raw.githubusercontent.com/jamescooke/factory_djoy/master/LICENSE

Factory Djoy
============

    Factories for Django, creating valid model instances every time.

Factory Djoy provides two simple classes, ``UserFactory`` and
``CleanModelFactory``, which wrap Factory Boy. They call ``full_clean()`` when
creating Django model instances to ensure that only valid data enters your
Django database.


Compatibility
-------------

Factory Djoy is compatible with:

* Django 2.2, 3.0 and 3.1

* Python 3 (3.7, 3.8, 3.9, 3.10, 3.11)

* Factory Boy version 2.11 or greater.


Resources
---------

* `Documentation on ReadTheDocs <https://factory-djoy.readthedocs.io/>`_

* `Package on PyPI <https://pypi.python.org/pypi/factory_djoy>`_

* `Source code on GitHub <https://github.com/jamescooke/factory_djoy>`_

* `Licensed on MIT <https://raw.githubusercontent.com/jamescooke/factory_djoy/master/LICENSE>`_

* `Changelog <https://github.com/jamescooke/factory_djoy/blob/master/CHANGELOG.rst>`_
