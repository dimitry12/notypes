# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='NoTypes',
    version='0.1.0',
    description='Types as notation for thought',
    long_description=readme,
    author='Dzmitry Pletnikau',
    url='https://github.com/dimitry12/notypes',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

