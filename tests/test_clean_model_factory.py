from django.core.exceptions import ValidationError
from django.test import TestCase
from factory.fuzzy import FuzzyText

from djoyapp.models import Item
from factory_djoy import CleanModelFactory


# Create a basic Factories for Item which can be used to test CleanModelFactory
# through because CleanModelFactory is abstract.
class SimpleItemFactory(CleanModelFactory):
    class Meta:
        model = Item


class ItemFactory(CleanModelFactory):
    class Meta:
        model = Item

    name = FuzzyText(length=5)


class FixedItemFactory(CleanModelFactory):
    class Meta:
        model = Item

    name = 'thing'


class TestSimpleItemFactory(TestCase):
    """
    Assert that invalid Item instances that could be created by factory are
    caught by full_clean.
    """

    def test_happy(self):
        """
        SimpleItemFactory can have required fields passed as kwargs
        """
        result = SimpleItemFactory(name='tap')

        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(result, Item.objects.filter(name='tap').first())

    def test_happy_build(self):
        """
        SimpleItemFactory can be built with invalid data
        """
        result = SimpleItemFactory.build()

        self.assertEqual(Item.objects.count(), 0)
        self.assertEqual(result.name, '')

    def test_happy_build_save(self):
        """
        SimpleItemFactory built instance can be saved to database
        """
        item = SimpleItemFactory.build()

        result = item.save()

        self.assertIsNone(result)
        self.assertEqual(Item.objects.count(), 1)

    def test_happy_build_not_clean(self):
        """
        SimpleItemFactory can be built with invalid data, can not full clean
        """
        item = SimpleItemFactory.build()

        with self.assertRaises(ValidationError) as cm:
            item.full_clean()

        self.assertEqual(Item.objects.count(), 0)
        self.assertEqual(list(cm.exception.error_dict), ['name'])

    # Invalidation cases

    def test_missing_name(self):
        """
        SimpleItemFactory does not autogenerate name and so fails validation
        """
        with self.assertRaises(ValidationError) as cm:
            SimpleItemFactory()

        self.assertEqual(['name'], list(cm.exception.error_dict.keys()))


class TestItemFactory(TestCase):

    def test_make_single(self):
        """
        ItemFactory can generate a name by default, that name is valid
        """
        result = ItemFactory()

        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(result, Item.objects.first())

    def test_make_multi(self):
        """
        ItemFactory can generate multiple items
        """
        ItemFactory.create_batch(2)

        self.assertEqual(Item.objects.count(), 2)


class TestFixedItemFactory(TestCase):

    def test_make_single(self):
        """
        FixedItemFactory makes Items with the same default name
        """
        result = FixedItemFactory()

        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(result, Item.objects.filter(name='thing').first())

    def test_duplicate(self):
        """
        FixedItemFactory can not create batch because duplicate name values
        """
        with self.assertRaises(ValidationError) as cm:
            FixedItemFactory.create_batch(2)

        self.assertEqual(list(cm.exception.error_dict), ['name'])

    def test_happy_build_no_name(self):
        """
        FixedItemFactory can be used to create an Item with an empty
        """
        item = FixedItemFactory.build(name='')

        result = item.save()

        self.assertIsNone(result)
        self.assertEqual(Item.objects.filter(name='').count(), 1)
        self.assertEqual(item.name, '')
