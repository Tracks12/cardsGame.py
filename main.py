#!/bin/python3
# -*- coding: utf-8 -*-

from os import system as shell
from platform import system
from sys import argv
from time import sleep

# Importation des dépendances internes
from core.icons import Icons
from core.region import Region
from core.cards import Cards
from core.games import *

def arg(reg): # Fonction d'entrée des arguments
	args = {
		"prfx": (
			(("-s", "--show-card"), "<x>"),
			(("-S", "--show-all"), ""),
			(("-r", "--show-rand"), ""),
			(("-h", "--help"), ""),
			(("-v", "--version"), "")
		),
		"desc": reg.content["args"]["desc"]
	}

	if(argv[1] in args["prfx"][-2][0]):
		for line in reg.content["args"]["intro"]:
			print(" {}".format(line))

		for i in range(0, len(args["prfx"])):
			print(" {}, {} {}\t{}".format(args["prfx"][i][0][0], args["prfx"][i][0][1], args["prfx"][i][1], args["desc"][i]))

	elif(argv[1] in args["prfx"][-1][0]):
		print(" cardsGame.py 0.1 {} Florian Cardinal\n".format(reg.content["vers"]))

	elif(argv[1] in args["prfx"][0][0]):
		packets = Cards()

		try:
			card = int(argv[2])

		except Exception:
			print("{}Spécifier un numéro de carte".format(Icons.warn))

			return False

		packets.getOneCard(card)

	elif(argv[1] in args["prfx"][1][0]):
		packets = Cards()
		packets.getAllCards()

	elif(argv[1] in args["prfx"][2][0]):
		packets = Cards()
		packets.mixCards()
		packets.getAllCards()

	return(True)

def main(reg): # Fonction principale de l'execution du programme
	game = PeckerLady(["admin", "root", "user"])
	game.start()

	return(True)

if __name__ == "__main__":
	reg = Region("fr")

	if(len(argv) > 1):
		arg(reg)

	else:
		main(reg)
