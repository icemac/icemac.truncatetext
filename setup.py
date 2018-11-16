# -*- coding: utf-8 -*-
# Copyright (c) 2009-2017 Michael Howitz
# See also LICENSE.txt

from setuptools import setup, find_packages
import os.path

version = '1.1.1'


def read(*path):
    """Read a file from a path."""
    return open(os.path.join(*path)).read()


setup(
    name='icemac.truncatetext',
    version=version,
    description='Nice, intelligent truncation of text.',
    long_description="\n\n".join([
        read("README.rst"),
        ".. contents::",
        read("icemac", "truncatetext", "README.rst"),
        read("CHANGES.rst"),
        read("HACKING.rst"),
    ]),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: German",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='text truncate string intelligent',
    author='Michael Howitz',
    author_email='icemac@gmx.net',
    url='https://github.com/icemac/icemac.truncatetext',
    license='MIT',
    packages=find_packages(),
    namespace_packages=['icemac'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
    ],
    test_suite="icemac.truncatetext.tests.test_all",
)
