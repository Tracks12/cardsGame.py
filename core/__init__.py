#!/bin/python3
# -*- coding: utf-8 -*-

from time import sleep

from core.b64 import B64
from core.cards import Cards
from core.config import Config
from core.colors import Colors
from core.icons import Icons
from core.players import LoadPlayers, Players
from core.regions import Regions

def splash(reg, info): # Splash Screen
	for row in tuple((
		"                      {}_        ______{}".format(Colors.yellow, Colors.end),
		"                     {}| |      / ____/{}".format(Colors.yellow, Colors.end),
		"  {}____ ___ _ _ __ ___| |  ___/ /   ___ ___ _ _ _ _ __   ___   ___{}".format(Colors.yellow, Colors.end),
		" {}/ __// _ ` | `_// _ ` | / _/ |   |_  / _ ` | `_` `_ \ / _ \ | _ \_ __{}".format(Colors.yellow, Colors.end),
		"{}| (__| (_)  | | | (_)  |_\ \ \ \___/ | (_)  | | | | | |  __/ |  _/\` /\t{}{}{}".format(Colors.yellow, Colors.red, info["vers"], Colors.end),
		" {}\__/ \___,_|_|  \___,_|___/  \_____/ \___,_|_| |_| |_|\___|.|_|  / /\t{}{} {}{}".format(Colors.yellow, Colors.purple, reg["COMMON_BY"], info["author"], Colors.end),
		"                                                                 {}/_/{}\n".format(Colors.yellow, Colors.end)
	)):
		print(row)
		sleep(.1)

	return(True)
