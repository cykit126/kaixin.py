#! /usr/bin/env python

from setuptools import setup, find_packages

setup(name='kaixin.py',
    version = '0.1.0',
    description = "kaixin.py is part of kaixin.dev. kaixin.dev is to make development happily.",
    author = "Wilbur Luo",
    author_email = "cykit126@gmail.com",
    url = "py.kaixindev.org",
    packages = find_packages(),
    package_data = {
        '': ['README']
    }
    keywords = "kaixin web"
)
