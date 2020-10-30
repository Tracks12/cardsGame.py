#!/bin/python3
# -*- coding: utf-8 -*-

import json
from os import system as shell
from platform import system
from sys import argv
from time import sleep

# Importation des dépendances internes
from core.icons import Icons
from core.regions import Regions
from core.cards import Cards
from core.games import *

def arg(reg): # Fonction d'entrée des arguments
	args = {
		"prfx": (
			(("-s", "--show-card"), "<x>"),
			(("-S", "--show-all"), ""),
			(("-r", "--show-rand-card"), "<x>"),
			(("-R", "--show-rand-all"), ""),
			(("-d", "--debug"), ""),
			(("-h", "--help"), ""),
			(("-v", "--version"), "")
		),
		"desc": reg.content["args"]["desc"]
	}

	if(argv[1] in args["prfx"][-2][0]):
		print(" {}".format(reg.content["args"]["intro"][0]))
		print(" {}: python main.py <arg>\n".format(reg.content["args"]["intro"][1]))
		print(" {}:".format(reg.content["args"]["intro"][2]))

		for i in range(0, len(args["prfx"])):
			print(" {}, {} {}\t{}".format(args["prfx"][i][0][0], args["prfx"][i][0][1], args["prfx"][i][1], args["desc"][i]))

	elif(argv[1] in args["prfx"][-1][0]):
		print(" cardsGame.py 0.1 {} Florian Cardinal\n".format(reg.content["vers"]))

	elif(argv[1] in args["prfx"][0][0]):
		packets = Cards()

		try:
			card = int(argv[2])-1

		except Exception:
			print("{}{}".format(Icons.warn, reg.content["args"]["err"]["cardNum"]))

			return False

		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][1][0]):
		packets = Cards()
		packets.dispAllCards()

	elif(argv[1] in args["prfx"][2][0]):
		packets = Cards()

		try:
			card = int(argv[2])-1

		except Exception:
			print("{}{}".format(Icons.warn, reg.content["args"]["err"]["cardNum"]))

			return False

		packets.mixCards()
		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][3][0]):
		packets = Cards()
		packets.mixCards()
		packets.dispAllCards()

	elif(argv[1] in args["prfx"][4][0]): # Mode Debugger
		isLinux = True if(system() == "Linux") else False

		while(True):
			shell("clear" if(isLinux) else "cls")
			shell("python{} main.py --help".format("3" if(isLinux) else ""))
			sleep(1)

	return(True)

def main(reg): # Fonction principale de l'execution du programme
	game = PeckerLady(["admin", "root", "user"], reg)
	game.start()

	return(True)

if __name__ == "__main__":
	try:
		with open("config.json") as outFile: # Importation du fichier de configuration
			config = json.load(outFile)
			reg = Regions(config["lang"])

	except Exception: # Paramétrage de la langue en anglais par défaut
		reg = Regions("us")

	if(len(argv) > 1):
		arg(reg)

	else:
		main(reg)
