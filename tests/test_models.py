from django.core.exceptions import ValidationError
from django.test import TestCase

from djoyapp.models import Item


class TestModels(TestCase):

    def test_happy(self):
        """
        Item instance can be created in test database
        """
        inst = Item(name='test')

        result = inst.save()

        self.assertIs(result, None)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(inst, Item.objects.first())

    def test_validation(self):  # noqa
        """
        Item model validates name requirements
        """
        with self.assertRaises(ValidationError) as cm:
            Item(name='carrot').full_clean()

        self.assertEqual(list(cm.exception.error_dict), ['name'])
