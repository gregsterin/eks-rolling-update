#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~
"""setup.py for affirm addresses."""

# import built-in
from __future__ import absolute_import
import os


from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read_file(file_name):
    file_path = os.path.join(here, file_name)
    return open(file_path, encoding='utf-8').read().strip()


setup(
    name='eks-rolling-update',
    version='1.0.0',
    description='EKS Rolling Update is a utility for updating the launch configuration or template of worker nodes in an EKS cluster.',
    long_description=read_file('README.md'),
    author='Craig Huber, Nicolas Bélanger, Sam Weston & contributors',
    author_email='ch@hellofresh.com',
    maintainer='Craig Huber & contributors',
    maintainer_email='ch@hellofresh.com',
    url='https://github.com/gregsterin/eks-rolling-update',
    license_file='LICENSE',
    licence='Apache License, Version 2.0',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "boto3>=1.9.246",
        "kubernetes>=10.0.1",
        "python-dotenv>=0.10.2"
    ],
    python_requires = ">=3.7",
    entry_points={
        # -*- Entry points -*-
        'console_scripts': ['eks_rolling_update.py=eksrollup.cli:main']
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
)
