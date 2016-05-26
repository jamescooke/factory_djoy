from django.contrib.auth import get_user_model
from factory import Sequence, PostGenerationMethodCall, SubFactory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    is_active = True
    is_staff = False
    is_superuser = False

    first_name = Sequence(lambda n: 'Joe{}'.format(n))
    last_name = Sequence(lambda n: 'Bloggs{}'.format(n))
    email = Sequence(lambda n: 'joe{}@bloggs.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'password')
