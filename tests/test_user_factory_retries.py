from django.contrib.auth import get_user_model
from django.test import TestCase
from mock import patch

from factory_djoy import UserFactory
from factory_djoy.factories import faker


class TestUserFactoryRetries(TestCase):

    model = get_user_model()

    def setUp(self):
        super(TestUserFactoryRetries, self).setUp()
        patcher = patch('factory_djoy.factories.faker.profile')
        m_profile = patcher.start()
        m_profile.side_effect = (
            {'username': 'zbeard'},
            {'username': 'vporter'},
            {'username': 'frobinson'},
        )
        self.addCleanup(patcher.stop)

    def test_set_up(self):
        """
        setUp: Faker has been seeded, creates Users with the same username
        """
        result = [UserFactory(), UserFactory(), UserFactory()]

        expected_usernames = ['zbeard', 'vporter', 'frobinson']
        self.assertEqual([user.username for user in result], expected_usernames)

    def test_retry(self):
        """
        UserFactory retries username generation in case of collision
        """
        self.model.objects.create(username='zbeard')

        result = UserFactory()

        self.assertEqual(result.username, 'vporter')
