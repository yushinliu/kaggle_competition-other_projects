#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is part of the python-chess library.
# Copyright (C) 2012-2014 Niklas Fiekas <niklas.fiekas@tu-clausthal.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import chess
import distutils
import os
import setuptools

def read_description():
    """
    Reads the description from README.rst and substitutes mentions of the
    latest version with a concrete version number.
    """
    description = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

    # Link to the documentation of the specific version.
    description = description.replace(
        "//python-chess.readthedocs.org/en/latest/",
        "//python-chess.readthedocs.org/en/v{0}/".format(chess.__version__))

    # Use documentation badge for the specific version.
    description = description.replace(
        "//readthedocs.org/projects/python-chess/badge/?version=latest",
        "//readthedocs.org/projects/python-chess/badge/?version=v{0}".format(chess.__version__))

    # Show Travis CI build status of the concrete version.
    description = description.replace(
        "//travis-ci.org/niklasf/python-chess.svg?branch=master",
        "//travis-ci.org/niklasf/python-chess.svg?branch=v{0}".format(chess.__version__))

    return description

setuptools.setup(
    name="python-chess",
    version=chess.__version__,
    author=chess.__author__,
    author_email=chess.__email__,
    description="A pure Python chess library with move generation and validation and handling of common formats.",
    long_description=read_description(),
    license="GPL3",
    keywords="chess fen pgn polyglot",
    url="https://github.com/niklasf/python-chess",
    packages=["chess"],
    scripts=["scripts/ecotool", "scripts/python-chess"],
    test_suite="test",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
