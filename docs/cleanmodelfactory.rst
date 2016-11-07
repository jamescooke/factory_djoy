CleanModelFactory
:::::::::::::::::

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

Side notes
++++++++++

* The ``ItemFactory`` example above is used in testing ``factory_djoy``. The
  ``models.py`` can be found in ``test_framework`` and the tests can be found
  in the ``tests`` folder.

* ``CleanModelFactory`` does not provide any ``get_or_create`` behaviour.
