UserFactory
:::::::::::

.. code-block:: python

    factory_djoy import UserFactory

``UserFactory`` provides valid instances of the default Django user at
``django.contrib.auth.User``.

As a result of the limitations around saving Users to the database in Django,
unique usernames are generated with a 3 step process:

Finally, the instance is checked with a call to ``full_clean``. This means that
if anything has gone wrong during generation, then a ``ValidationError`` will
be raised. This also means that values that might be passed into the Factory
are tested for validity:

.. code-block:: python

    >>> UserFactory(username='user name')
    Traceback (most recent call last):
    ...
    ValidationError: {'username': ['Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.']}


Given a simple test that requires a User instance, ``UserFactory`` can generate
that at test time. All validated fields have valid values created for them.
This example is a bit contrived, but it works:

.. code-block:: python

    >>> from django.test import Client
    >>> UserFactory(username='user_1', password='test')
    >>> assert Client().login(username='user_1', password='test')


Invalid / unsaved data
======================

If you need to create invalid data in your tests, then the ``build`` strategy
is available:

.. code-block:: python

    >>> user = UserFactory.build(username='user name')
    >>> user.id is None
    True
    >>> user.full_clean()
    Traceback (most recent call last):
    ...
    ValidationError: {'username': ['Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.']}
    >>> user.save()
