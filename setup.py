#!/usr/bin/env python
#encoding=utf-8


from setuptools import setup, find_packages


setup(
    name='ZoomEye',
    version='0.0.1',
    description='ZoomEye Undocumented API',
    license='GPL v3.0',
    url='https://github.com/issmall/ZoomEye',

    author='issmall',
    author_email='i55m411@sina.com',

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        'requests',
        'six',
    ],
)

