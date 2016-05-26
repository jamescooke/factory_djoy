import os
import setuptools


setuptools.setup(
    name='factory_djoy',
    version='0.1',
    description="Wrappers over Factory Boy's Django Factories",
    url='http://github.com/jamescooke/factory_djoy',
    author='James Cooke',
    author_email='github@jamescooke.info',
    license='MIT',
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
