#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============
Roman Numerals
==============

:website: https://github.com/jambonrose/roman-numerals
:copyright: Copyright 2017 Andrew Pinkham
:license: Simplified BSD, see LICENSE for details.
"""

from codecs import open as codec_open
from os import path

from setuptools import find_packages, setup

HERE = path.abspath(path.dirname(__file__))


# Get the long description from the Read Me
with codec_open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Get test dependencies
TEST_REQS = 'requirements/test_requirements.txt'
with codec_open(path.join(HERE, TEST_REQS), encoding='utf-8') as f:
    TESTS_REQUIRE = f.read().splitlines()

# Get test dependencies
INSTALL_REQS = 'requirements/install_requirements.txt'
with codec_open(path.join(HERE, INSTALL_REQS), encoding='utf-8') as f:
    INSTALL_REQUIRE = f.read().splitlines()

setup(
    name='roman-numerals',
    version='0.0.1',  # PEP 440 Compliant Semantic Versioning
    keywords=['text', 'roman', 'numerals', 'convert'],
    description=(
        'A library to convert between integers'
        ' and Unicode Roman numerals.'
    ),
    long_description=LONG_DESCRIPTION,
    url='https://github.com/jambonrose/roman-numerals',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,

    setup_requires=['pytest-runner'],
    install_requires=INSTALL_REQUIRE,
    test_suite='tests',
    tests_require=TESTS_REQUIRE,

    author='Andrew Pinkham',
    author_email='hello at andrewsforge dot com',

    license='Simplified BSD License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
)
