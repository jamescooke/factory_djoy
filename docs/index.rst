Factory Djoy
::::::::::::

.. image:: https://circleci.com/gh/jamescooke/factory_djoy.svg?style=shield
    :target: https://circleci.com/gh/jamescooke/factory_djoy
.. image:: https://img.shields.io/pypi/pyversions/factory_djoy.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/factory_djoy
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/jamescooke/factory_djoy/master/LICENSE

Factories for Django, creating valid model instances every time.

Simple wrappers around Factory Boy for Django which call ``full_clean`` when
creating instances to ensure that only valid data enters your Django database.

Compatible with:

* Latest flavours of Django 1.8, 1.9 and 1.10.

* Python 2.7, 3.4 and 3.5.

* Factory Boy version 2 or greater.


Contents
--------

.. toctree::
   :maxdepth: 2

   quickstart
   userfactory
   cleanmodelfactory
   motivation
   contribution
   development


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
