#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='color-extractor',
    version='1.0',
    description='An util to extract the main colors from an image',
    author='Maciej Bratek',
    author_email='maclav3@gmail.com',
    url='https://github.com/maclav3/py-extract-colors',
    packages=['color_extractor'],
    requires=[
        'Pillow', 'numpy', 'webcolors', ],
    entry_points={
        'console_scripts': [
            'color-extractor = color_extractor.__main__:main'
        ]
    }
)
