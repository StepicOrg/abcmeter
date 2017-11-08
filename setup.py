from os.path import join, dirname

from setuptools import setup, find_packages

setup(
    name='ABC Meter',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'antlr4-python3-runtime==4.7',
        'typing==3.6.2',
    ],
)
