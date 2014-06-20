#!/usr/bin/env python


import setuptools
from distutils.core import setup
import os, sys

# Dynamically calculate the version based on colors.VERSION.
version = __import__('colors').get_version()

setup(
    name = 'Django Colors (fork)',
    version = version.replace(' ', '-'),
    description = 'Manipulate colors with django',
    author = 'Florian Chiș', 'Maxime Haineault',
    author_email = 'florian.chis@gmail.com', 'max@motion-m.ca',
    url = 'https://github.com/Fl0r14n/django-colors',
    packages = ['colors'],
)

