# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2024, Damian Birchler
#
# Licensed under the terms of the GNU General Public License v3
# ----------------------------------------------------------------------------
"""
Pytrnsys setup.
"""
from setuptools import find_packages
from setuptools import setup

from spyder_pytrnsys import __version__


setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="spyder-pytrnsys",
    version=__version__,
    author="Damian Birchler",
    author_email="damian.birchler@ost.ch",
    description="Pytrnsys GUI for Spyder",
    license="GNU General Public License v3",
    url="https://github.com/zuckerruebe/spyder-pytrnsys",
    python_requires='>= 3.7',
    install_requires=[
        "qtpy",
        "qtawesome",
        "spyder>=5.0.1",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "spyder_pytrnsys = spyder_pytrnsys.spyder.plugin:Pytrnsys"
        ],
    },
    classifiers=[
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
