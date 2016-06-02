from django.contrib.auth import get_user_model
from factory import LazyFunction, PostGenerationMethodCall, post_generation
from factory.django import DjangoModelFactory
from faker.factory import Factory as FakerFactory


faker = FakerFactory.create()


class CleanModelFactory(DjangoModelFactory):
    """
    Ensures that created instances pass Django's `full_clean` checks.

    NOTE: may not work with `get_or_create`.
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
    username = LazyFunction(lambda: faker.profile()['username'])

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
