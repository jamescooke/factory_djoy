Factory Djoy
============

.. image:: https://circleci.com/gh/jamescooke/factory_djoy.svg?style=shield
    :target: https://circleci.com/gh/jamescooke/factory_djoy

Simple wrappers on top of Factory Boy for Django.

Works on latest flavour of Django 1.9 with Python 3.4.

Testing first
-------------

Primarily the goal of factories is to provide "easy to generate" data at test
time - however this data must be 100% reliable, otherwise it's too easy to
create false positive and false negative test results.

Therefore, since it's so important that each factory creates valid data,
these wrappers are tested rigorously using Django projects configured in the
``test_framework`` folder.

See also
--------

* `Development documentation <DEV.rst>`_ for info on how to build, test and
  upload.
* `django-factory_boy <https://github.com/rbarrois/django-factory_boy>`_ which
  has more of Django's stock models covered, but has less tests.

License
-------

`MIT <LICENSE>`_
