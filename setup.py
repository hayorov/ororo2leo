#!/usr/bin/env python

import os

from pip.req import parse_requirements
from setuptools import setup

install_reqs = parse_requirements(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                               'requirements.txt'), session='None')

setup(
    name='ororo2leo',
    author='Sasha Khaerov',
    version='0.0.1',
    keywords='ororo.tv ororo lingualeo export import tool dictionary words',
    packages=['ororo2leo'],
    description='A command line tool for exporting ororo.tv dictionary to lingualeo',
    url='https://github.com/hayorov/ororo2leo',
    license='Apache Software License',
    install_requires=[str(ir.req) for ir in install_reqs],
    entry_points={
        'console_scripts': [
            'ororo2leo = ororo2leo.ororo2leo:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',

        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],
)
