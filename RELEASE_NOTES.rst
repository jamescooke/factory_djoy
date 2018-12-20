Release Notes
=============

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_ and
this project adheres to `Semantic Versioning <http://semver.org/>`_.

Unreleased_
-----------

See also `latest documentation
<http://factory-djoy.readthedocs.io/en/latest/>`_.

1.0.1_ - 2018/12/20
-------------------

This will be the last release to support Django 1 and Python 2.

Changed
:::::::

* Updated support for Django 1.11 to latest release.

1.0.0_ - 2018/04/20
-------------------

Added
:::::

* Support Django 1.11 and Python 3.6.

Removed
:::::::

* Support for unsupported versions of Django 1.8, 1.9, 1.10.

* Support for Python 3.4.

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

.. _Unreleased: https://github.com/jamescooke/factory_djoy/compare/v1.0.1...HEAD
.. _1.0.1: https://github.com/jamescooke/factory_djoy/compare/v1.0.0...v1.0.1
.. _1.0.0: https://github.com/jamescooke/factory_djoy/compare/v0.6.0...v1.0.0
.. _0.6.0: https://github.com/jamescooke/factory_djoy/compare/v0.5.0...v0.6.0
.. _0.5.0: https://github.com/jamescooke/factory_djoy/compare/v0.4...v0.5.0
.. _0.4: https://github.com/jamescooke/factory_djoy/compare/v0.3...v0.4
