# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from divio_wagtail_puput import __version__


setup(
    name='divio-wagtail-puput',
    version=__version__,
    description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'puput==0.8',
    ],
    include_package_data=True,
    zip_safe=False,
)
