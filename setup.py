#!/usr/bin/env python2
from distutils.core import setup 
from setuptools import find_packages

from os import path

# Try to build doc, converting from language markdown to rst using pandoc if it is installed
import platform
import subprocess
import os
import sys

CUR_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

version = "1.2.16"

                                                    

py_version = platform.python_version_tuple()

convert_the_doc_command = "pandoc --from=markdown --to=rst --output=" + os.path.join(CUR_DIR_PATH, "README.rst") + " " + os.path.join(CUR_DIR_PATH, "README.md")

# subprocess has check_output since python 2.7.0+
if py_version <= (2, 6, 9):
    try:
        result = os.popen(convert_the_doc_command)
    except Exception, e:
        pass
else:
    try:
        result = subprocess.check_output(convert_the_doc_command , shell=True)
    except Exception, e:
        pass





here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(name='jsonpyes',
        version=version,
        author="Alexander Liu",
        author_email='PGP E6DE7BEA',
        license="GPL V3",
        description="Import JSON raw data to ElasticSearch using Python in one line of commands",
        long_description=long_description,
        platforms=["Unix","Linux","OSX","Android","Windows"],
        url="https://github.com/xros/jsonpyes",
        download_url="https://github.com/xros/jsonpyes/tarball/" + version,
        #py_modules=['elasticsearch','jsonpyes','simplejson'],
        install_requires=[
            'elasticsearch',
            'simplejson',
        ],
        keywords=["elasticsearch","json","json2es","jsonpyes"],
        classifiers=[],
        # Make this script executable in command line
        #scripts=['jsonpyes.py'],
        scripts=['jsonpyes', 'jsonpyes.py'],
        #packages=['contrib', ],
        packages=find_packages(),
        include_package_data=True,
)
