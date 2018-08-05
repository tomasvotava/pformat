#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pformat.py
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

import sys

"""
PrettyFormat printer.
1.0
Available for tty(s) only.
"""

PFORMAT_ATTRIBUTES = {
	"red":		"\033[91m",
	"-":		"\033[0m\033[39m\033[49m",
	"bold":		"\033[1m",
	"dim":		"\033[2m",
	"black":	"\033[30m",
	"green":	"\033[92m",
	"yellow":	"\033[93m",
	"blue":		"\033[94m",
	"magenta":	"\033[95m",
	"cyan":		"\033[96m",
	"white":	"\033[97m",
	"bblack":	"\033[40m",
	"bred":		"\033[41m",
	"bgreen":	"\033[42m",
	"bwhite":	"\033[107m",
	"normal":	"\033[0m"
}

def tty_supports_color():
    """
    Returns True if the running system's terminal supports color, and False
    otherwise.
    Source: https://stackoverflow.com/questions/7445658/how-to-detect-if-the-console-does-support-ansi-escape-codes-in-python
    Thanks
    """
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                  'ANSICON' in os.environ)
    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    if not supported_platform or not is_a_tty:
        return False
    return True


def pformat(string):
	"""
	Returns string PFormatted.
	"""
	for att in PFORMAT_ATTRIBUTES:
		string = string.replace(":%s:"%att,PFORMAT_ATTRIBUTES[att] if tty_supports_color() else "")
	return (string+(PFORMAT_ATTRIBUTES["-"] if tty_supports_color() else ""))

def pprint(string):
	"""
	Prints PFormatted string.
	"""
	print(pformat(string))

def pinput(prompt):
	"""
	Gets input from user, prompt is PFormatted.
	"""
	return input(pformat(prompt))
