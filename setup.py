# -*- coding: utf-8 -*-
# Copyright (c) 2009-2010 Michael Howitz
# See also LICENSE.txt

from setuptools import setup, find_packages
import os.path

version = '0.3dev'

def read(*path):
    return open(os.path.join(*path)).read() + "\n\n"


setup(name='icemac.truncatetext',
      version=version,
      description=read("README.txt"),
      long_description=(
        read("README.txt") +
        ".. contents::\n\n" +
        read("icemac", "truncatetext", "README.txt") +
        read("CHANGES.txt")),
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.3",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='text truncate string intelligent',
      author='Michael Howitz',
      author_email='icemac@gmx.net',
      url='http://pypi.python.org/pypi/icemac.truncatetext',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['icemac'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'setuptools',
        ],
      test_suite="icemac.truncatetext.tests.test_all",
      )
