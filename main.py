#!/bin/python3
# -*- coding: utf-8 -*-

import json
from os import system as shell
from platform import system
from sys import argv
from time import sleep

# Importation des dépendances internes
from core.colors import Colors
from core.icons import Icons
from core.regions import Regions
from core.cards import Cards
from core.games import *

def splash(reg, info): # Splash Screen
	for l in [
		"                      {}_        ______{}".format(Colors.yellow, Colors.end),
		"                     {}| |      / ____/{}".format(Colors.yellow, Colors.end),
		"  {}____ ___ _ _ __ ___| |  ___/ /   ___ ___ _ _ _ _ __   ___   ___{}".format(Colors.yellow, Colors.end),
		" {}/ __// _ ` | `_// _ ` | / _/ |   |_  / _ ` | `_` `_ \ / _ \ | _ \_ __{}".format(Colors.yellow, Colors.end),
		"{}| (__| (_)  | | | (_)  |_\ \ \ \___/ | (_)  | | | | | |  __/ |  _/\` /\t{}{}{}".format(Colors.yellow, Colors.red, info["version"], Colors.end),
		" {}\__/ \___,_|_|  \___,_|___/  \_____/ \___,_|_| |_| |_|\___|.|_|  / /\t{}{} {}{}".format(Colors.yellow, Colors.purple, reg.content["vers"], info["author"], Colors.end),
		"                                                                 {}/_/{}\n".format(Colors.yellow, Colors.end)
	]:
		print(l)
		sleep(.1)

	return True

def arg(reg, info): # Fonction d'entrée des arguments
	args = {
		"prfx": (
			(("-s", "--show-card"), "<x>"),
			(("-S", "--show-all"), ""),
			(("-r", "--show-rand-card"), "<x>"),
			(("-R", "--show-rand-all"), ""),
			(("-h", "--help"), ""),
			(("-d", "--debug"), ""),
			(("-v", "--version"), "")
		),
		"desc": reg.content["args"]["desc"]
	}

	if(argv[1] in args["prfx"][-3][0]): # Affiche le helper args
		print(" {}".format(reg.content["args"]["intro"][0]))
		print(" {}: python main.py <arg>\n".format(reg.content["args"]["intro"][1]))
		print(" {}:".format(reg.content["args"]["intro"][2]))

		for i in range(0, len(args["prfx"])):
			print(" {}, {} {}\t{}".format(args["prfx"][i][0][0], args["prfx"][i][0][1], args["prfx"][i][1], args["desc"][i]))

	elif(argv[1] in args["prfx"][-2][0]): # Mode Debugger
		isLinux = True if(system() == "Linux") else False

		while(True):
			shell("clear" if(isLinux) else "cls")
			shell("python{} main.py --help".format("3" if(isLinux) else ""))
			sleep(1)

	elif(argv[1] in args["prfx"][-1][0]): # Affiche la version du script
		print(" cardsGame.py 0.1 {} Florian Cardinal\n".format(reg.content["vers"]))

	elif(argv[1] in args["prfx"][0][0]): # Affiche une carte du paquet
		packets = Cards()

		try:
			card = int(argv[2])-1

		except Exception:
			print("{}{}".format(Icons.warn, reg.content["err"]["cardNum"]))

			return False

		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][1][0]): # Affiche tout le paquet
		packets = Cards()
		packets.dispAllCards()

	elif(argv[1] in args["prfx"][2][0]): # Affiche une carte du paquet mélangé
		packets = Cards()

		try:
			card = int(argv[2])-1

		except Exception:
			print("{}{}".format(Icons.warn, reg.content["err"]["cardNum"]))

			return False

		packets.mixCards()
		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][3][0]): # Affiche tout le paquet mélangé
		packets = Cards()
		packets.mixCards()
		packets.dispAllCards()

	return(True)

def main(reg, info): # Fonction principale de l'execution du programme
	splash(reg, info)

	game = PeckerLady(["admin", "root", "user"], reg)
	game.start()

	return(True)

if __name__ == "__main__":
	info = {
		"version": "0.1",
		"author": "Florian Cardinal"
	}

	try:
		with open("config.json") as outFile: # Importation du fichier de configuration
			config = json.load(outFile)
			reg = Regions(config["lang"])

	except Exception: # Paramétrage de la langue en anglais par défaut
		reg = Regions("us")
		print("{}{}".format(Icons.warn, reg.content["err"]["regLoad"]))
		print("{}{}".format(Icons.info, reg.content["tip"]["regLoad"]))

	if(len(argv) > 1):
		arg(reg, info)

	else:
		main(reg, info)
