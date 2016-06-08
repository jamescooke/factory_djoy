Factory Djoy
::::::::::::

.. image:: https://circleci.com/gh/jamescooke/factory_djoy.svg?style=shield
    :target: https://circleci.com/gh/jamescooke/factory_djoy
.. image:: https://img.shields.io/pypi/pyversions/factory_djoy.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/factory_djoy
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/jamescooke/factory_djoy/master/LICENSE

Simple wrappers around Factory Boy for Django which call ``full_clean`` when
creating instances to ensure that only valid data enters your Django database.

Works on latest flavours of Django 1.8 and 1.9, with Factory Boy version 2 or
greater.


Installation
============

Install with ``pip``::

    pip install factory_djoy


Usage
=====

``CleanModelFactory``
---------------------

This is a generic wrapper for ``DjangoModelFactory``. It provides all the
functionality of ``DjangoModelFactory`` but extends ``create`` to call
``full_clean`` at post-generation time. This validation ensures that your test
factories only create instances that meet your models' field level and model
level validation requirements - this leads to better tests.

Example
.......

Given a very simple model called ``Item`` which has one name field that is
required and has a max length of 5 characters:

.. code-block:: python

    class Item(Model):
        """
        Single Item with one required field 'name'
        """
        name = CharField(max_length=5, unique=True)

Then we can create a clean factory for it using ``CleanModelFactory``:

.. code-block:: python

    from factory_djoy import CleanModelFactory

    from yourapp.models import Item


    class SimpleItemFactory(CleanModelFactory):
        class Meta:
            model = Item

Now we haven't defined any default value for the ``name`` field, so if we use
this factory with no keyword arguments then ``ValidationError`` is raised:

.. code-block:: python

    >>> SimpleItemFactory()
    Traceback (most recent call last):
    ...
    django.core.exceptions.ValidationError: {'name': ['This field cannot be blank.']}

However, if we pass a valid name, then everything works OK:

.. code-block:: python

    >>> SimpleItemFactory(name='tap')

Automatically generating values
...............................

The point of using ``CleanModelFactory`` is not to make testing harder because
lots of keyword arguments are needed for each factory call, instead it should
be easier and more reliable. Really the work with ``SimpleItemFactory`` above
is not complete.

Now we replace ``SimpleItemFactory`` with a new ``ItemFactory`` that generates
the required ``name`` field by default. We're going to use ``factory_boy``'s
`Fuzzy attributes <http://factoryboy.readthedocs.io/en/latest/fuzzy.html>`_ to
generate random default values each time the model is instantiated and because
``full_clean`` is called every time an instance is created, we will know that
every instance passed validation.

.. code-block:: python

    from factory.fuzzy import FuzzyText
    from factory_djoy import CleanModelFactory


    class ItemFactory(CleanModelFactory):
        class Meta:
            model = Item

        name = FuzzyText(length=5)

Now we can happily generate multiple instances of ``Item`` leaving the factory
to create random names for us.

.. code-block:: python

    >>> item = ItemFactory()
    >>> item.name
    'TcEBK'

Alternatively, if you wanted all your created ``Item`` instances to have the
name value for ``name`` each time, you can just set that in the factory
declaration.

.. code-block:: python

    class FixedItemFactory(CleanModelFactory):
        class Meta:
            model = Item

        name = 'thing'

However, in this instance, you will receive ``ValidationErrors`` because
``name`` is expected to be unique.

.. code-block:: python

    >>> FixedItemFactory.create_batch(2)
    Traceback (most recent call last):
    ...
    django.core.exceptions.ValidationError: {'name': ['Item with this Name already exists.']}

``full_clean`` is triggered only with the ``create`` strategy. Therefore using
``build`` followed by ``save`` can provide a way to emulate "bad" data in your
Django database if that's required. In this example, we can create an ``Item``
instance without a ``name``.

.. code-block:: python

    >>> item = FixedItemFactory.build(name='')
    >>> item.save()
    >>> assert item.id

After saving successfully, if ``full_clean`` is called then the saved ``Item``
will fail validation because it does not have a ``name``:

.. code-block:: python

    >>> item.full_clean()
    Traceback (most recent call last):
    ...
    django.core.exceptions.ValidationError: {'name': ['This field cannot be blank.']}

*Side note:* The ``ItemFactory`` example above is used in testing
``factory_djoy``. The ``models.py`` can be found in ``test_framework`` and the
tests can be found in the ``tests`` folder.


``UserFactory``
---------------

.. code-block:: python

    >>> from factory_djoy import UserFactory

``UserFactory`` provides a simple wrapper over the ``django.contrib.auth.User``
model which validates the generated User instance with ``full_clean`` before
it is saved. You can use it anywhere that you need a User instance to be
created in your project's factories.

Given a simple test that requires a User instance, ``UserFactory`` can generate
that at test time. All validated fields have valid values created for them.
This example is a bit contrived, but it works:

.. code-block:: python

    >>> from django.test import Client
    >>> UserFactory(username='user_1', password='test')
    >>> assert Client().login(username='user_1', password='test')

The field-level validation built in to ``UserFactory`` requires that the
``User.username`` field only contains certain permitted characters. Therefore
``UserFactory`` will raise ``ValidationError`` if it attempts to create a
``User`` instance with an invalid ``username``, or any other field value:

.. code-block:: python

    >>> UserFactory(username='user name')
    Traceback (most recent call last):
    ...
    ValidationError: {'username': ['Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.']}

Same as with ``CleanModelFactory``, the ``build`` strategy is available if
tests require invalid data:

.. code-block:: python

    >>> UserFactory.build(username='user name').save()


Motivation: Testing first
=========================

Primarily the goal of factories is to provide "easy to generate" data at test
time - however this data must be 100% reliable, otherwise it's too easy to
create false positive and false negative test results. By calling
``full_clean`` on every Django instance that is built, this helps to create
certainty in the data used by tests - the instances will be valid as if they
were created through the default Django admin.

Therefore, since it's so important that each factory creates valid data,
these wrappers are tested rigorously using Django projects configured in the
``test_framework`` folder.


Contribution
============

* Please see `Issues <https://github.com/jamescooke/factory_djoy/issues/>`_.
  There are a number of outstanding tasks.

* Please ensure that any provided code:

  * Has been developed with "test first" process.

  * Can be auto-merged in GitHub.

  * Passes testing on Circle CI.


See also
========

* `Development documentation
  <https://github.com/jamescooke/factory_djoy/blob/master/DEV.rst>`_ for info
  on how to build, test and upload.

* `django-factory_boy <https://github.com/rbarrois/django-factory_boy>`_ which
  implements more factories for Django's stock models, but doesn't validate
  generated instances and has less tests.

* `Django's model save vs full_clean
  <http://jamescooke.info/djangos-model-save-vs-full_clean.html>`_ for an
  explanation of how Django can screw up your data when saving.
