#!/usr/bin/env python2

from distutils.core import setup
from os.path import abspath
from os.path import join as path_join
from os import getcwd
from shutil import rmtree

import CryptoCoinChartsApi

pathname		=		getcwd()

packages        =       ['CryptoCoinChartsApi']

setup(name		    =		'CryptoCoinChartsApi',
      version		=		'0.0.1',
      description	=		'Python API for www.cryptocoincharts.info',
      author		=		'Dirrot',
      author_email  =       'dirrot@web.de',
      url		    =		'https://github.com/Dirrot/python-cryptocoincharts-api',
      packages		=		packages,
      package_dir	=		{'CryptoCoinChartsApi.py' : abspath(path_join(pathname, 'CryptoCoinChartsApi/'))},
      data_files	=		[('share/CryptoCoinChartsApi', ['README.md', 'LICENSE', 'img/donation-qr-code.png'])],

	)


try:
	rmtree(abspath(path_join(pathname, 'build/')))
except:
	pass
