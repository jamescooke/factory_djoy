Motivation
::::::::::

Testing first
=============

Primarily the goal of factories is to provide "easy to generate" data at test
time - however this data must be 100% reliable, otherwise it's too easy to
create false positive and false negative test results. By calling
``full_clean`` on every Django instance that is built, this helps to create
certainty in the data used by tests - the instances will be valid as if they
were created through the default Django admin.

Therefore, since it's so important that each factory creates valid data,
these wrappers are tested rigorously using Django projects configured in the
``test_framework`` folder.

See also
========

* `django-factory_boy <https://github.com/rbarrois/django-factory_boy>`_ which
  implements more factories for Django's stock models, but doesn't validate
  generated instances and has less tests.

* `Django Factory Audit <http://jamescooke.info/django-factory-audit.html>`_
  which compares every Django factory library I could find with respect to how
  they create valid instances.

* `Django's model save vs full_clean
  <http://jamescooke.info/djangos-model-save-vs-full_clean.html>`_ for an
  explanation of how Django can screw up your data when saving.
