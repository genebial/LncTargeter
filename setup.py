#!usr/bin/env pytohn
# -*- coding:utf-8 -*-

from src import utils as ut
from setuptools import setup
from setuptools import find_packages

requirments = [
            "biopython>=1.79",
            "certifi>=2020.6.20",
            "numpy>=1.21.2",
            "pandas>=1.3.4",
            "python-dateutil>=2.8.2",
            "pytz>=2021.3",
            "scipy>=1.7.1",
            "six>=1.16.0",
            "xgboost>=1.5.0",
]

setup(name='LncTarget',
      version=ut.get_version(),
      author="Qingran Kong, Weibo Hou",
      author_email="",
      packages=find_packages(),
      scripts=['LncTarget'],
      include_package_data=True,
      url="",
      license="LICENSE",
      description="Framework for predicting LncRNA binding sites and their potential regulatory genes",
      # long_description=open('README.rst').read(),
      install_requires=requirments,
      python_requires=">=3.8",
      zip_safe=False,
      platforms=['Linux']
      )
