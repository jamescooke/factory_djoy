from django.db.models import Model
from django.db.models.fields import CharField


class Item(Model):
    """
    Single Item with one required field 'name'
    """
    name = CharField(max_length=5, unique=True)
