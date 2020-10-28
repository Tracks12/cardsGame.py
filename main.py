#!/bin/python3
# -*- coding: utf-8 -*-

from sys import argv

# Importation des dépendances internes
from core.cards import Cards

def arg():
	args = {
		"prfx": (
			(("-h", "--help"), ""),
			(("-v", "--version"), "")
		),
		"desc": (
			"\tAffichage du menu d'aide",
			"\tAffichage de la version du programme\n"
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



	return(True)

def main():
	packets = Cards()
	packets.getAllCards()

	return(True)

if __name__ == "__main__":
	if(len(argv) > 1):
		arg()

	else:
		main()
