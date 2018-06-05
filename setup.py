import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "okschema",
    version = "0.1.0",
    author = "Krzysztof Stachlewski",
    author_email = "stach@stachlewski.info",
    description = "json validation library",
    license = "BSD",
    url = "http://packages.python.org/okschema", # TODO: gh
    packages=['okschema'],
    long_description=read('README.md'),
)