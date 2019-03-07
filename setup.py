# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup, find_packages

import pyacc as pkg

exclude = ['.idea*', 'build*', '{}.egg-info*'.format(pkg.__package__), 'dist*', 'venv*', 'doc*', 'lab*']

requirements = Path.cwd().joinpath('requirements.txt')
dependency_links = list()

if requirements.exists:
    requirements = requirements.read_text()
    requirements = [r.strip() for r in requirements.split('\n')]
else:
    requirements = list()

classifiers = [
    'Development Status :: 5 - Production',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

setup(
    name=pkg.__package__,
    version=pkg.__version__,
    packages=find_packages(exclude=exclude),
    entry_points={
        'console_scripts': [
            'pyacc = pyacc.main:run'
        ]
    },
    url=pkg.__site__,
    license=pkg.__license__,
    keywords=pkg.__keywords__,
    author=pkg.__author__,
    author_email=pkg.__email__,
    long_description=pkg.__long_description__,
    description=pkg.__description__,
    classifiers=classifiers,
    install_requires=requirements,
    dependency_links=dependency_links
)
