from django.contrib.auth import get_user_model
from django.test import TestCase

from factory_djoy import UserFactory


class TestUserFactory(TestCase):

    user_model = get_user_model()

    def test_user_default_password(self):
        """
        UserFactory sets a usable password as 'password' by default

        Built user is also active
        """
        UserFactory()

        self.assertEqual(self.user_model.objects.count(), 1)
        user = self.user_model.objects.first()
        self.assertTrue(user.check_password('password'))
        self.assertTrue(user.is_active)

    def test_user_custom_password(self):
        """
        UserFactory can be passed a custom password and sets it
        """
        UserFactory(password='cstm_3$!&vBA.,QokHuva')

        user = self.user_model.objects.first()
        self.assertTrue(user.check_password('cstm_3$!&vBA.,QokHuva'))

    def test_user_factory_create_unusable_pw(self):
        """
        UserFactory can create a user with an unusable password
        """
        UserFactory(password=None)

        user = self.user_model.objects.first()
        self.assertFalse(user.has_usable_password())
        self.assertTrue(user.is_active)

    def test_happy(self):
        """
        UserFactory can generate User that can log in as per README

        README doctring: User can log in
        """
        UserFactory(username='user_1', password='test')

        result = self.client.login(username='user_1', password='test')

        self.assertIs(result, True)
