#!/usr/bin/env python3
import pathlib
from setuptools import setup, Extension
from Cython.Build import cythonize

# The directory containing this file
root_dir = pathlib.Path(__file__).parent

# The text of the README file
README = (root_dir / "README.md").read_text()

setup(
    name="python-libfprint",
    version="0.0.1",
    description="A fprint library wrapper",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Diego Saraiva",
    author_email="diegosaraiva@gmail.com",
    package_dir={'python-libfprint': 'lib'},
    packages=['python-libfprint'],
    ext_modules=cythonize([
        Extension("fprint",
            sources=["lib/fprint.pyx"],
            libraries=["fprint"]),
        ]
    ),
    package_data={
        '': ['*.pyx', '*.pxd', '*.c'],
    },
    project_urls={
        "Source": "https://github.com/jdiego/python-libfprint",
    }
)
