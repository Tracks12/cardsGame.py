#!/bin/python3
# -*- coding: utf-8 -*-

from sys import argv
from time import sleep

# Importation des dépendances internes
from core.icons import Icons
from core.cards import Cards
from core.games import *

def arg(): # Fonction d'entrée des arguments
	args = {
		"prfx": (
			(("-s", "--show-card"), "<x>"),
			(("-S", "--show-all"), ""),
			(("-r", "--show-rand"), ""),
			(("-h", "--help"), ""),
			(("-v", "--version"), "")
		),
		"desc": (
			"\tAffiche une carte",
			"\tAffiche toutes les cartes",
			"\tAffiche toutes les cartes mélanger\n",
			"\tAffiche le menu d'aide",
			"\tAffiche la version du programme\n"
		)
	}

	if(argv[1] in args["prfx"][-2][0]):
		print(" Jeux de cartes")
		print(" Lancement: python main.py <arg>\n")
		print(" Arguments:")

		for i in range(0, len(args["prfx"])):
			print(" {}, {} {}\t{}".format(args["prfx"][i][0][0], args["prfx"][i][0][1], args["prfx"][i][1], args["desc"][i]))

	elif(argv[1] in args["prfx"][-1][0]):
		print(" cardsGame.py 0.1 - Florian Cardinal\n")

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

def main(): # Fonction principale de l'execution du programme
	game = PeckerLady(2, ["admin", "root"])

	game.start()

	return(True)

if __name__ == "__main__":
	if(len(argv) > 1):
		arg()

	else:
		main()
