from six import advance_iterator

from django.contrib.auth import get_user_model
from factory import (
    LazyFunction,
    PostGenerationMethodCall,
    lazy_attribute,
    post_generation,
)
from factory.django import DjangoModelFactory
from faker.factory import Factory as FakerFactory

faker = FakerFactory.create(providers=[])
max_retries = 200


class CleanModelFactory(DjangoModelFactory):
    """
    Ensures that created instances pass Django's `full_clean` checks.
    """
    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Call `full_clean` on any created instance before saving
        """
        obj = model_class(*args, **kwargs)
        obj.full_clean()
        obj.save()
        return obj


class UserFactory(DjangoModelFactory):
    """
    Factory for default Django User model. Calls full_clean before saving to
    ensure that generated User instance is valid.
    """
    class Meta:
        model = get_user_model()

    email = LazyFunction(faker.safe_email)
    first_name = LazyFunction(faker.first_name)
    last_name = LazyFunction(faker.last_name)
    password = PostGenerationMethodCall('set_password', 'password')

    @lazy_attribute
    def username(self):
        """
        Create a username from faker's profile generator, but ensure that it's
        not in the database before using it. This is a pre-full_clean check.

        Uses a simple single uniqueness check, cached against a set of already
        tried names. 200 max tries is on the username generation, not the round
        trip to the database - although that could be changed if required.

        Raises:
            RuntimeError: If a unique username can not be found after 200
                retries.
        """
        unique_usernames = unique_username()
        non_uniques = set()
        for _ in range(max_retries):
            username = advance_iterator(unique_usernames)
            username_unique = (
                username not in non_uniques and
                get_user_model().objects.filter(username=username).count() == 0
            )
            if username_unique:
                return username
            non_uniques.add(username)
        else:
            non_uniques_str = ', '.join(['"{}"'.format(name) for name in non_uniques])
            message = (
                'Unique username not found after 200 tries. Unique values tried: {}'
            ).format(non_uniques_str)
            raise RuntimeError(message)

    @post_generation
    def z_full_clean(self, create, extracted, **kwargs):
        """
        Assert that created User is "clean" in Django's opinion if build
        strategy is happening.

        NOTE: function name is prefixed with 'z_' so that it runs after the
        'password' post generation function.

        Raises:
            ValidationError: If there are any invalid fields in the final User
                object.
        """
        if create:
            self.full_clean()


def unique_username():
    """
    Generate a unique username. Keeps a set of previously generated usern
    """
    used = set()
    while(True):
        username = faker.user_name()
        if username not in used:
            used.add(username)
            yield username
