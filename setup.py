#!/usr/bin/env python

from distutils.core import setup

setup(name='PyHTTPServer',
      version='1.0',
      description='A simple HTTP Server package for python3',
      author='KMikeeU',
      author_email='mikeeu@pm.me',
      url='https://github.com/KMikeeU/PyHTTPServer',
      packages=['PyHTTPServer'],
      install_requires=["re", "socket", "ssl", "_thread"]
     )