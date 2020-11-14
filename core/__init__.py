#!/bin/python3
# -*- coding: utf-8 -*-

from base64 import b64decode, b64encode
from platform import system
from time import sleep

class Colors: # Module de coloration pour les système Linux/Unix
	if(system() == "Linux"):
		bold	= "\033[1m"
		italic	= "\033[3m"

		red		= "\033[31m"
		green	= "\033[32m"
		yellow	= "\033[33m"
		blue	= "\033[34m"
		purple	= "\033[35m"
		cyan	= "\033[36m"
		white	= "\033[37m"

		end		= "\033[0m"

	else:
		bold = italic = end = ""
		red = green = yellow = blue = purple = cyan = white = ""

class Icons: # Module d'icône ascii
	warn = " {}{}[!]{} - ".format(Colors.bold, Colors.red, Colors.end)
	info = " {}{}(i){} - ".format(Colors.bold, Colors.blue, Colors.end)
	tips = " {}{}(?){} - ".format(Colors.bold, Colors.green, Colors.end)
	play = " {}{}(>){} - ".format(Colors.bold, Colors.green, Colors.end)

class B64: # Encode/Decode ascii string
        def encode(str = ""):
                return(b64encode(str.encode("ascii")).decode("ascii"))

        def decode(str = ""):
                return(b64decode(str).decode("ascii"))

def splash(reg, info): # Splash Screen
	for row in [
		"                      {}_        ______{}".format(Colors.yellow, Colors.end),
		"                     {}| |      / ____/{}".format(Colors.yellow, Colors.end),
		"  {}____ ___ _ _ __ ___| |  ___/ /   ___ ___ _ _ _ _ __   ___   ___{}".format(Colors.yellow, Colors.end),
		" {}/ __// _ ` | `_// _ ` | / _/ |   |_  / _ ` | `_` `_ \ / _ \ | _ \_ __{}".format(Colors.yellow, Colors.end),
		"{}| (__| (_)  | | | (_)  |_\ \ \ \___/ | (_)  | | | | | |  __/ |  _/\` /\t{}{}{}".format(Colors.yellow, Colors.red, info["vers"], Colors.end),
		" {}\__/ \___,_|_|  \___,_|___/  \_____/ \___,_|_| |_| |_|\___|.|_|  / /\t{}{} {}{}".format(Colors.yellow, Colors.purple, reg["vers"], info["author"], Colors.end),
		"                                                                 {}/_/{}\n".format(Colors.yellow, Colors.end)
	]:
		print(row)
		sleep(.1)

	return(True)
