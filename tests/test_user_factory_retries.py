import unittest

from django.contrib.auth import get_user_model
from django.test import TestCase

from factory_djoy import UserFactory
from factory_djoy.factories import unique_username

from unittest.mock import patch


class TestUserFactoryRetries(TestCase):

    model = get_user_model()

    def setUp(self):
        super(TestUserFactoryRetries, self).setUp()
        patcher = patch('factory_djoy.factories.unique_username')
        self.m_unique_username = patcher.start()
        self.addCleanup(patcher.stop)

    def test_set_up(self):
        """
        setUp: Faker has been seeded, creates Users with the same username
        """
        self.m_unique_username.return_value = (x for x in ('zbeard', 'vporter', 'frobinson'))

        result = [UserFactory(), UserFactory(), UserFactory()]

        expected_usernames = ['zbeard', 'vporter', 'frobinson']
        self.assertEqual([user.username for user in result], expected_usernames)

    def test_retry(self):
        """
        UserFactory retries username generation in case of collision
        """
        self.m_unique_username.return_value = (x for x in ('zbeard', 'vporter'))
        self.model.objects.create(username='zbeard')

        result = UserFactory()

        self.assertEqual(result.username, 'vporter')

    def test_retry_cap(self):  # noqa
        """
        UserFactory will only retry 200 times, then raises RuntimeError
        """
        profile_values = ('zbeard',) * 200
        profile_values += (ValueError('201st call'),)
        self.m_unique_username.return_value = (x for x in profile_values)
        self.model.objects.create(username='zbeard')

        with self.assertRaises(RuntimeError) as cm:
            UserFactory()

        self.assertEqual(self.model.objects.count(), 1)
        message = cm.exception.args[0]
        self.assertIn('Unique username not found', message)
        self.assertIn('Unique values tried: "zbeard"', message)


class TestUniqueUsername(unittest.TestCase):

    def test_happy(self):
        """
        unique_username wrapper is able to provide 2000 unique names

        This appears to take around 1000ms on a crappy toaster using 1 core.
        """
        unique_username_gen = unique_username()

        result = {next(unique_username_gen) for _ in range(2000)}

        self.assertEqual(len(result), 2000)
