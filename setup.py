import os

from setuptools import find_packages, setup

basedir = os.path.dirname(__file__)


def readme():
    with open(os.path.join(basedir, 'README.rst')) as f:
        return f.read()


about = {}
with open(os.path.join(basedir, 'factory_djoy', '__about__.py')) as f:
    exec(f.read(), about)


setup(
    name=about['__name__'],
    version=about['__version__'],

    description=about['__description__'],
    long_description=readme(),
    long_description_content_type="text/x-rst",
    url='http://github.com/jamescooke/factory_djoy',
    author=about['__author__'],
    author_email=about['__email__'],

    license='MIT',

    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'Django>=2.2',
        'factory_boy>=2.11',
    ],
    python_requires='>=3.7',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
)
