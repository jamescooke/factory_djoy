from .settings import *  # NOQA


# Django 1.8 still has INSTALLED_APPS as a tuple
INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append('djoyapp')
