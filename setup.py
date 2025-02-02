# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dns_updater',
    version='1.0.0',
    description='',
    long_description=readme,
    author='sknutsen',
    author_email='',
    url='https://github.com/sknutsen/DNSUpdater',
    license=license,
    packages=find_packages()
)

