UserFactory
:::::::::::

.. code-block:: python

    from factory_djoy import UserFactory

``UserFactory`` provides valid instances of the default Django user at
``django.contrib.auth.User``. By default it creates valid users with unique
usernames, random email addresses and populated first and last names.

.. code-block:: python

    >>> user = UserFactory()
    >>> user.username
    'cmcmahon'
    >>> user.email
    'amandajones@example.com'
    >>> user.first_name + ' ' + user.last_name
    'Tiffany Hoffman'

Just as with ``factory_boy``, the API can be used to create instances with
specific data when required:

.. code-block:: python

    >>> user = UserFactory(first_name='René')
    >>> user.first_name
    'René'


Passwords
=========

In order to be able to use the generated User's password, then pass one to the
factory at generation time, otherwise the randomly generated password will be
hashed and lost. The ``UserFactory`` correctly uses ``set_password`` to set the
password for the created User instance.

.. code-block:: python

    >>> from django.test import Client
    >>> user = UserFactory(password='test')
    >>> assert Client().login(username=user.username, password='test')

If you want a User that can not log in, then pass ``None`` as the password.

.. code-block:: python

    >>> user = UserFactory(password=None)
    >>> user.has_usable_password()
    False


Unique usernames
================

The factory will try up to 200 times per instance to generate a unique
username.

As a result of the limitations around saving Users to the database in Django,
these unique usernames are generated with a 3 step process:

* Ask ``faker`` for a random username. Compare it to those generated already
  and use it if its unique.

* Ensure that the picked username is not already in the Django database.

* Create instance with planned unique username and check the generated instance
  with a call to ``full_clean``. This means that if anything has gone wrong
  during generation, then a ``ValidationError`` will be raised. This also means
  that values that might be passed into the Factory are tested for validity:

  .. code-block:: python

      >>> UserFactory(username='user name')
      Traceback (most recent call last):
      ...
      ValidationError: {'username': ['Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.']}


Invalid data
============

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
