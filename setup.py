# -*- coding: utf-8 -*-
# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='icemac.truncatetext',
      version=version,
      description="Nice, intelligent truncation of text.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Programming Language :: Python",
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
