Installation and Quick Start
::::::::::::::::::::::::::::

Installation
============

Easiest is to install with ``pip``::

    pip install factory_djoy

Quick Start
===========

Factory Djoy provides a ``UserFactory`` out of the box which will build valid
instances of the default `Django contrib auth
<https://docs.djangoproject.com/en/dev/ref/contrib/auth/#user-model>`_ ``User``
model.

.. code-block:: python

    from factory_djoy import UserFactory

    user = UserFactory()

For any other Django models that you would like valid instances for, create
your factory by inheriting from ``CleanModelFactory``.

.. code-block:: python

    from factory_djoy import CleanModelFactory

    from project.app.models import Item


    class ItemFactory(CleanModelFactory):
        class Meta:
            model = Item
