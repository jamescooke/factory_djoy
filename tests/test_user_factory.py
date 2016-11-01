from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from factory_djoy import UserFactory


class TestUserFactory(TestCase):

    user_model = get_user_model()

    def test_make_single(self):
        """
        UserFactory can make a single User

        * Names and email are generated by Fuzzy and are more than the empty
            string.
        * Default password is 'password'.
        """
        result = UserFactory()

        self.assertEqual(self.user_model.objects.count(), 1)
        user = self.user_model.objects.first()
        self.assertEqual(result, user)
        self.assertGreater(user.username, '')
        self.assertGreater(user.first_name, '')
        self.assertGreater(user.last_name, '')
        self.assertGreater(user.email, '')
        self.assertTrue(user.check_password('password'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_make_multi(self):
        """
        UserFactory can create two Users with default settings using batch

        Only username is unique between instances.
        """
        UserFactory.create_batch(2)

        self.assertEqual(self.user_model.objects.count(), 2)
        user_first = self.user_model.objects.first()
        user_last = self.user_model.objects.last()
        self.assertNotEqual(user_first.username, user_last.username)

    def test_make_multi_large(self):
        """
        UserFactory can generate 1000 users

        For all generated users, assert that they are valid after creation
        """
        UserFactory.create_batch(1000)

        self.assertEqual(self.user_model.objects.count(), 1000)
        for user in self.user_model.objects.all():
            user.full_clean()

    def test_custom_password(self):
        """
        UserFactory can be passed a custom password and sets it
        """
        UserFactory(password='custom$password')

        user = self.user_model.objects.first()
        self.assertTrue(user.check_password('custom$password'))

    def test_create_unusable_pw(self):
        """
        UserFactory can create a user with an unusable password
        """
        UserFactory(password=None)

        user = self.user_model.objects.first()
        self.assertFalse(user.has_usable_password())
        self.assertTrue(user.is_active)

    def test_no_email(self):
        """
        UserFactory can create user without email address
        """
        UserFactory(email='')

        user = self.user_model.objects.first()
        self.assertEqual(user.email, '')

    def test_inactive(self):
        """
        UserFactory can create inactive user
        """
        UserFactory(is_active=False)

        user = self.user_model.objects.first()
        self.assertFalse(user.is_active)

    def test_staff(self):
        """
        UserFactory can create staff user
        """
        UserFactory(is_staff=True)

        user = self.user_model.objects.first()
        self.assertTrue(user.is_staff)

    def test_superuser(self):
        """
        UserFactory can create superuser user
        """
        UserFactory(is_superuser=True)

        user = self.user_model.objects.first()
        self.assertTrue(user.is_superuser)

    def test_documentation(self):
        """
        UserFactory can generate User that can log in as per README

        README doctring: User can log in
        """
        UserFactory(username='user_1', password='test')

        result = self.client.login(username='user_1', password='test')

        self.assertIs(result, True)

    def test_build(self):
        """
        UserFactory can build a User without validating
        """
        result = UserFactory.build(username='BAD USER')

        self.assertEqual(self.user_model.objects.count(), 0)
        self.assertEqual(result.username, 'BAD USER')

    def test_build_save(self):
        """
        UserFactory can be saved with invalid data if build is used
        """
        user = UserFactory.build(username='bad user')

        result = user.save()

        self.assertIsNone(result)
        self.assertEqual(self.user_model.objects.count(), 1)
        self.assertEqual(self.user_model.objects.get(username='bad user'), user)

    # Invalidation cases

    def test_fail_integrity(self):
        """
        UserFactory will raise IntegrityError saving to DB with missing field
        """
        with self.assertRaises(IntegrityError):
            UserFactory(first_name=None)

    def test_fail_validation_first_name(self):
        """
        UserFactory with first name too long will fail validation

        Django limits first names to 30 characters.
        """
        with self.assertRaises(ValidationError) as cm:
            UserFactory(first_name=31*'a')

        self.assertEqual(list(cm.exception.error_dict), ['first_name'])

    def test_fail_validation_last_name(self):
        """
        UserFactory with last name too long will fail validation

        Django limits last names to 30 characters.
        """
        with self.assertRaises(ValidationError) as cm:
            UserFactory(last_name=31*'a')

        self.assertEqual(list(cm.exception.error_dict), ['last_name'])

    def test_fail_validation_username(self):
        """
        UserFactory will fail with invalid username
        """
        with self.assertRaises(ValidationError) as cm:
            UserFactory(username='user name')

        self.assertEqual(list(cm.exception.error_dict), ['username'])

    def test_fail_username_override(self):
        """
        UserFactory will raise IntegrityError when username is collided
        """
        existing_user = UserFactory()

        with self.assertRaises(IntegrityError):
            UserFactory(username=existing_user.username)
