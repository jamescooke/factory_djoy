from django.contrib.auth import get_user_model
from django.test import TestCase

from factory_djoy import UserFactory

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestUserFactoryRetries(TestCase):

    model = get_user_model()

    def setUp(self):
        super(TestUserFactoryRetries, self).setUp()
        patcher = patch('factory_djoy.factories.faker.profile')
        self.m_profile = patcher.start()
        self.addCleanup(patcher.stop)

    def test_set_up(self):
        """
        setUp: Faker has been seeded, creates Users with the same username
        """
        self.m_profile.side_effect = (
            {'username': 'zbeard'},
            {'username': 'vporter'},
            {'username': 'frobinson'},
        )

        result = [UserFactory(), UserFactory(), UserFactory()]

        expected_usernames = ['zbeard', 'vporter', 'frobinson']
        self.assertEqual([user.username for user in result], expected_usernames)

    def test_retry(self):
        """
        UserFactory retries username generation in case of collision
        """
        self.m_profile.side_effect = (
            {'username': 'zbeard'},
            {'username': 'vporter'},
        )
        self.model.objects.create(username='zbeard')

        result = UserFactory()

        self.assertEqual(result.username, 'vporter')

    def test_retry_cap(self):
        """
        UserFactory will only retry 200 times, then raises RuntimeError
        """
        profile_values = ({'username': 'zbeard'},) * 200
        profile_values += (ValueError('201st call'),)
        self.m_profile.side_effect = profile_values
        self.model.objects.create(username='zbeard')

        with self.assertRaises(RuntimeError) as cm:
            UserFactory()

        self.assertEqual(self.model.objects.count(), 1)
        message = cm.exception.args[0]
        self.assertIn('Unique username not found', message)
        self.assertIn('Unique values tried: "zbeard"', message)
