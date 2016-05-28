Factory Djoy
::::::::::::

.. image:: https://circleci.com/gh/jamescooke/factory_djoy.svg?style=shield
    :target: https://circleci.com/gh/jamescooke/factory_djoy
.. image:: https://img.shields.io/pypi/pyversions/factory_djoy.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/factory_djoy
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/jamescooke/factory_djoy/master/LICENSE

Simple wrappers on top of Factory Boy for Django. Works on latest flavour of
Django 1.9, with Factory Boy version 2 or greater.


Installation
============

Install with ``pip``::

    pip install factory_djoy


Usage
=====

``UserFactory``
---------------

``UserFactory`` provides a simple wrapper over the ``django.contrib.auth.User``
model. You can use it anywhere that you need a User instance to be created in
your project's factories.

Given a simple test that requires a User instance, ``UserFactory`` can generate
that at test time. This example is a bit contrived, but it works:

.. code-block:: python

    from django.test import TestCse
    from factory_djoy import UserFactory


    class TestUser(TestCase):

        def test_happy(self):
            """
            User can log in
            """
            UserFactory(username='user_1', password='test')

            result = self.client.login(username='user_1', password='test')

            self.assertIs(result, True)


Motivation: Testing first
=========================

Primarily the goal of factories is to provide "easy to generate" data at test
time - however this data must be 100% reliable, otherwise it's too easy to
create false positive and false negative test results.

Therefore, since it's so important that each factory creates valid data,
these wrappers are tested rigorously using Django projects configured in the
``test_framework`` folder.


See also
========

* `Development documentation
  <https://github.com/jamescooke/factory_djoy/blob/master/DEV.rst>`_ for info
  on how to build, test and upload.
* `django-factory_boy <https://github.com/rbarrois/django-factory_boy>`_ which
  implements more factories for Django's stock models, but has less tests.
