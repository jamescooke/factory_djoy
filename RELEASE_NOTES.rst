Release Notes
=============

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_ and
this project adheres to `Semantic Versioning <http://semver.org/>`_.

0.6.0_ - 2016/11/20
-------------------

Added
:::::

* Improve ``UserFactory`` so that it can generate unique usernames using Faker
  and checking against Django's database before saving the instance.

* `Documentation added <https://factory-djoy.readthedocs.io/>`_.

Fixed
:::::

* Bug `username collision bug
  <https://github.com/jamescooke/factory_djoy/issues/15>`_ in ``UserFactory``.

0.5.0_ - 2016/10/22
-------------------

Added
:::::

* Bump support for Django up to 1.10, add it to the test suite.

0.4_ - 2016/08/06
-----------------

Added
:::::

* Allow ``build`` to bypass full clean. Allows creation of invalid data.

0.3 - 2016/05/10
-----------------

Stable testing release.

.. _0.6.0: https://github.com/jamescooke/factory_djoy/compare/v0.5.0...v0.6.0
.. _0.5.0: https://github.com/jamescooke/factory_djoy/compare/v0.4...v0.5.0
.. _0.4: https://github.com/jamescooke/factory_djoy/compare/v0.3...v0.4
