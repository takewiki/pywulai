#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    reshapedata LLC
"""
import platform
from setuptools import setup
from setuptools import find_packages

setup(
    name = 'pywulai',
    version = '1.0.1',
    install_requires=[
        'requests','pyrda'
    ],
    packages=find_packages(),
    license = 'Apache License',
    author = 'Reshapedata',
    author_email = 'hulilei@takewiki.com.cn',
    url = 'http://www.reshapedata.com',
    description = 'reshape data wu lai open api in py language ',
    keywords = ['reshapedata', 'rdwulai'],
    python_requires='>=3.6',
)
