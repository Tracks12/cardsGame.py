#!/bin/python3
# -*- coding: utf-8 -*-

# Module de coloration pour les système Linux/Unix

from json import load
from os.path import abspath
from platform import system

from core.constants import ENABLE_COLOR

try:
	with open(abspath("config.json"), "r", encoding="utf-8") as cfgFile:
		_ = dict[str, str | bool](load(cfgFile))
		ENABLE_COLOR = _["colors"]

except:
	pass

class Colors:
	if(ENABLE_COLOR):
		bold	= str("\033[1m")
		italic	= str("\033[3m")

		red	= str("\033[31m")
		green	= str("\033[32m")
		yellow	= str("\033[33m")
		blue	= str("\033[34m")
		purple	= str("\033[35m")
		cyan	= str("\033[36m")
		white	= str("\033[37m")

		end	= str("\033[0m")

	else:
		bold = italic = end = str("")
		red = green = yellow = blue = purple = cyan = white = str("")