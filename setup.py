#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  setup.py
#  
#  Copyright 2018 Tomáš Votava <info@tomasvotava.eu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from setuptools import setup, find_packages
setup(
	name="PFormat",
	version="1.2",
	#packages=[],
	py_modules=["pformat"],
	author="Tomas Votava",
	author_email="info@tomasvotava.eu",
	description="Simple Color Printing for TTYs in Python",
	license="GNU/GPL",
	keywords="printing color tty",
	url="https://github.com/tomasvotava/pformat"
)
