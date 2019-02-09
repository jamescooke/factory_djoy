from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.fields import CharField, EmailField, IntegerField


class Item(Model):
    """
    Single Item with one required field 'name'
    """
    name = CharField(max_length=5, unique=True)


class Material(Model):
    """
    Model used to check validation with multiple fields
    """
    name = CharField(max_length=64)
    strength = IntegerField()

    def clean(self):
        """
        If material is stronger than 100, then it must have "strong" in name
        """
        if self.strength > 100 and 'strong' not in self.name:
            raise ValidationError('Material is strong, but not called "strong"')
