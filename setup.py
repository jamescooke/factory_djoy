import os
import setuptools


setuptools.setup(
    name='factory_djoy',
    version='0.3',

    description="Wrappers around Factory Boy's Django Factories",
    url='http://github.com/jamescooke/factory_djoy',
    author='James Cooke',
    author_email='github@jamescooke.info',

    license='MIT',

    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'Django>=1.8',
        'factory_boy>=2.7',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
