from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='icemac.truncatetext',
      version=version,
      description="Nice, intelligent truncation of text.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
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
