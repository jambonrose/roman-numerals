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


def load_file_contents(file_path, as_list=True):
    """Load file as string or list"""
    abs_file_path = path.join(HERE, file_path)
    with codec_open(abs_file_path, encoding='utf-8') as file_pointer:
        if as_list:
            return file_pointer.read().splitlines()
        return file_pointer.read()


# Get the long description from the Read Me
LONG_DESCRIPTION = load_file_contents('README.rst', as_list=False)
# Get test dependencies
TESTS_REQUIRE = load_file_contents('requirements/test_requirements.txt')

setup(
    name='roman-numerals',
    version='0.1.0',  # PEP 440 Compliant Semantic Versioning
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
    extras_require={
        ':python_version < "3.5"': [
            'typing==3.6.1',
        ],
    },
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
