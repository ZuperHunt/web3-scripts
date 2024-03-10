from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Collection of web3 scripts'
LONG_DESCRIPTION = 'A general collection of web3 scripts for interaction'

# Setting up
setup(
    name="zuperscripts",
    version=VERSION,
    author="Zuperhunt",
    author_email="nurmuhammadluthfi@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'transaction', 'web3', 'scripts'],
    license="MIT",
    url="https://github.com/nmluthfi/web3-scripts.git",
    project_urls={
        'Source': 'https://github.com/nmluthfi/web3-scripts.git',
    },
)
