Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_ and
this project adheres to `Semantic Versioning <http://semver.org/>`_.

Unreleased_
-----------

See also `latest documentation
<http://factory-djoy.readthedocs.io/en/latest/>`_.

Added
:::::

* Explicit support for Pythons 3.9, 3.10 and 3.11 added. `#104
  <https://github.com/jamescooke/factory_djoy/issues/104>`_

Changed
:::::::

* Python code upgraded with ``pyupgrade`` to Python 3.7 and above. `#116
  <https://github.com/jamescooke/factory_djoy/pull/116>`_

2.2.1_ - 2022/10/22
-------------------

Removed
:::::::

* Dropped support for Python 3.6. `#109
  <https://github.com/jamescooke/factory_djoy/pull/109>`_

* Dropped support for Django 1.11. `#97
  <https://github.com/jamescooke/factory_djoy/issues/97>`_

* Compiled requirements for Django versions removed, tox trusted to install
  good versions. `#111
  <https://github.com/jamescooke/factory_djoy/issues/111>`_

2.2.0_ - 2021/03/08
-------------------

Removed
:::::::

* Support for Python 3.5. `#98
  <https://github.com/jamescooke/factory_djoy/pull/98>`_

Changed
:::::::

* CI moved from Travis to GitHub actions. `#101
  <https://github.com/jamescooke/factory_djoy/pull/101>`_

2.1.4_ - 2021/01/03
-------------------

Added
:::::

* Explicit support for Django 3.1. `#91
  <https://github.com/jamescooke/factory_djoy/pull/91>`_

2.1.3_ - 2020/01/19
-------------------

Added
:::::

* Explicit support for Django 3.0 . `#73
  <https://github.com/jamescooke/factory_djoy/pull/73>`_

Removed
:::::::

* Support for Django 2.1.

2.1.2_ - 2019/11/23
-------------------

Added
:::::

* Explicit support for Python 3.8 with Python 3.8 added to test framework.

* Test runs extended to include Django 2.2 on Pythons 3.5 and 3.6.

2.1.1_ - 2019/04/06
-------------------

Added
:::::

* Django 2.2 now added to test framework.

2.1.0_ - 2019/02/10
-------------------

Added
:::::

* Expanded information in stack traces when ``CleanModelFactory`` fails to
  create a valid instance because ``full_clean()`` failed.

2.0.0_ - 2018/12/31
-------------------

Added
:::::

* Explicit support for Django 2.1.

* Explicit support for Python 3.7.

Removed
:::::::

* Support for Python 2.7.


1.0.2_ - 2018/12/21
-------------------

Added
:::::

* ``python_requires`` to help pip find the Python 2 version.

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

.. _Unreleased: https://github.com/jamescooke/factory_djoy/compare/v2.2.1...HEAD
.. _2.2.1: https://github.com/jamescooke/factory_djoy/compare/v2.2.0...v2.2.1
.. _2.2.0: https://github.com/jamescooke/factory_djoy/compare/v2.1.4...v2.2.0
.. _2.1.4: https://github.com/jamescooke/factory_djoy/compare/v2.1.3...v2.1.4
.. _2.1.3: https://github.com/jamescooke/factory_djoy/compare/v2.1.2...v2.1.3
.. _2.1.2: https://github.com/jamescooke/factory_djoy/compare/v2.1.1...v2.1.2
.. _2.1.1: https://github.com/jamescooke/factory_djoy/compare/v2.1.0...v2.1.1
.. _2.1.0: https://github.com/jamescooke/factory_djoy/compare/v2.0.0...v2.1.0
.. _2.0.0: https://github.com/jamescooke/factory_djoy/compare/v1.0.2...v2.0.0
.. _1.0.2: https://github.com/jamescooke/factory_djoy/compare/v1.0.1...v1.0.2
.. _1.0.1: https://github.com/jamescooke/factory_djoy/compare/v1.0.0...v1.0.1
.. _1.0.0: https://github.com/jamescooke/factory_djoy/compare/v0.6.0...v1.0.0
.. _0.6.0: https://github.com/jamescooke/factory_djoy/compare/v0.5.0...v0.6.0
.. _0.5.0: https://github.com/jamescooke/factory_djoy/compare/v0.4...v0.5.0
.. _0.4: https://github.com/jamescooke/factory_djoy/compare/v0.3...v0.4
