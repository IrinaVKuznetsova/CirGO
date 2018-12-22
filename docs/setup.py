#!/usr/bin/env python


# Implementation is based on:
# https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html#towelstuff-description

from setuptools import setup        # supports "install_requires" parameter
#from distutils.core import setup   # https://stackoverflow.com/questions/24727709/do-python-projects-need-a-manifest-in-and-what-should-be-in-it

  
 
 
setup(name='CirGO', 
      version='0.1.0',
      description='Python, GOs Visualization Software ', 
      keywords='visualization', 
      url='https://github.com/IrinaVKuznetsova/CirGO', 
      author='Irina Kuznetsova', 
      author_email='irina.kuznetsova@uwa.edu.au', 
      license='GPL-3.0', 
      install_requires=[
        "numpy == 1.13.1",
        "matplotlib == 2.1.0",
	"argparse == 1.1"
    ],
)
