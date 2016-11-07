UserFactory
:::::::::::

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
