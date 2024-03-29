#!/usr/bin/env python

# Adapted from
# https://github.com/FSund/pygments-custom-cpplexer/blob/master/setup.py

from setuptools import setup, find_packages

setup(
    name='pygments-ppddl',
    description='Pygments lexer PPDDL',
    long_description=open('README.md').read(),
    keywords='pygments lexer ppddl',
    version='0.0.1'
    packages=find_packages(),
    install_requires=['pygments >= 2.0'],
    entry_points='[pygments.lexers]\nppddl=pygments_ppddl:PPDDLLexer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Plugins',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
