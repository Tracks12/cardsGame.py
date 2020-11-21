#!/bin/python3
# -*- coding: utf-8 -*-

from base64 import b64decode, b64encode
from platform import system
from time import sleep

class Colors: # Module de coloration pour les système Linux/Unix
	if(system() == "Linux"):
		bold	= str("\033[1m")
		italic	= str("\033[3m")

		red		= str("\033[31m")
		green	= str("\033[32m")
		yellow	= str("\033[33m")
		blue	= str("\033[34m")
		purple	= str("\033[35m")
		cyan	= str("\033[36m")
		white	= str("\033[37m")

		end		= str("\033[0m")

	else:
		bold = italic = end = str("")
		red = green = yellow = blue = purple = cyan = white = str("")

class Icons: # Module d'icône ascii
	warn = str(f" {Colors.bold}{Colors.red}[!]{Colors.end} - ")
	info = str(f" {Colors.bold}{Colors.blue}(i){Colors.end} - ")
	tips = str(f" {Colors.bold}{Colors.green}(?){Colors.end} - ")
	play = str(f" {Colors.bold}{Colors.green}(>){Colors.end} - ")

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
