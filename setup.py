# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "mux_python"
VERSION = "1.5.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Official Mux API wrapper for python projects 🐍.",
    author_email="sdks@mux.com",
    url="https://github.com/muxinc/mux-python",
    download_url="https://github.com/muxinc/mux-python/archive/1.5.0.tar.gz",
    keywords=["Mux Video", "Video", "Live Stream", "VOD", "Streaming"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Official Mux API wrapper for python projects 🐍.
    Not familiar with Mux? Check out https://mux.com/ for more information.
    """
)
