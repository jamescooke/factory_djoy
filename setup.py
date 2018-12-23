import os
from setuptools import setup, find_packages

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
    url='http://github.com/jamescooke/factory_djoy',
    author=about['__author__'],
    author_email=about['__email__'],

    license='MIT',

    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'Django>=1.11',
        'factory_boy>=2.7',
    ],
    python_requires='>=3.5',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
)
