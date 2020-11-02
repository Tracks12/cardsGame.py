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
	for row in [
		"                      {}_        ______{}".format(Colors.yellow, Colors.end),
		"                     {}| |      / ____/{}".format(Colors.yellow, Colors.end),
		"  {}____ ___ _ _ __ ___| |  ___/ /   ___ ___ _ _ _ _ __   ___   ___{}".format(Colors.yellow, Colors.end),
		" {}/ __// _ ` | `_// _ ` | / _/ |   |_  / _ ` | `_` `_ \ / _ \ | _ \_ __{}".format(Colors.yellow, Colors.end),
		"{}| (__| (_)  | | | (_)  |_\ \ \ \___/ | (_)  | | | | | |  __/ |  _/\` /\t{}{}{}".format(Colors.yellow, Colors.red, info["vers"], Colors.end),
		" {}\__/ \___,_|_|  \___,_|___/  \_____/ \___,_|_| |_| |_|\___|.|_|  / /\t{}{} {}{}".format(Colors.yellow, Colors.purple, reg.content["vers"], info["author"], Colors.end),
		"                                                                 {}/_/{}\n".format(Colors.yellow, Colors.end)
	]:
		print(row)
		sleep(.1)

	return(True)

def arg(cfg, reg, info, games): # Fonction d'entrée des arguments
	args = {
		"prfx": (
			(("-s", "--show-card"), "<x>"),
			(("-S", "--show-all"), ""),
			(("-r", "--show-rand-card"), "<x>"),
			(("-R", "--show-rand-all"), ""),
			(("-g", "--game"), "<gameName>"),
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
			shell("python{} main.py".format("3" if(isLinux) else ""))
			input("{}{}".format(Icons.info, reg.content["debug"]["continue"]))

	elif(argv[1] in args["prfx"][-1][0]): # Affiche la version du script
		print(" {} {} {} {}\n".format(info["name"], info["vers"], reg.content["vers"], info["author"]))

	elif(argv[1] in args["prfx"][0][0]): # Affiche une carte du paquet
		packets = Cards(2)

		try:
			card = int(argv[2])-1

		except Exception:
			print("{}{}".format(Icons.warn, reg.content["err"]["cardNum"]))

			return(False)

		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][1][0]): # Affiche tout le paquet
		packets = Cards(2)
		packets.dispAllCards()

	elif(argv[1] in args["prfx"][2][0]): # Affiche une carte du paquet mélangé
		packets = Cards(2)

		try:
			card = int(argv[2])-1

		except Exception:
			print("{}{}".format(Icons.warn, reg.content["err"]["cardNum"]))

			return(False)

		packets.mixCards()
		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][3][0]): # Affiche tout le paquet mélangé
		packets = Cards(2)
		packets.mixCards()
		packets.dispAllCards()

	elif(argv[1] in args["prfx"][4][0]): # Lance un mode de jeu choisis en arguments
		try:
			gameName = str(argv[2])

		except Exception:
			print("{}{}".format(Icons.warn, reg.content["err"]["gameName"]))

			return(False)

		gameList = []
		for game in games:
			gameList.append(game([], reg).gameName)

		for id, name in enumerate(gameList):
			if(gameName == name):
				game = games[id](["admin", "root"], reg)
				print("{}{}".format(Icons.play, game.gameName))

				if(not game.finished):
					print("{}{}".format(Icons.warn, reg.content["game"]["notFinished"]))

				game.start()

	return(True)

def main(cfg, reg, info, games): # Fonction principale de l'execution du programme
	menu = [ "{}:\n".format(reg.content["menu"]["txt"]) ]

	if(cfg["splash"]):
		splash(reg, info)

	for game in games:
		menu.append(game([], reg).gameName)

	for key, row in enumerate(menu):
		print(" {}{}".format("" if(key == 0) else "{}{}.{} ".format(Colors.cyan, key, Colors.end), row))

	print("")
	#print( " {}{}.{} {}".format(Colors.yellow, len(menu), Colors.end, reg.content["menu"]["set"]))
	print( " {}0.{} {}\n".format(Colors.red, Colors.end, reg.content["menu"]["quit"]))

	while(True):
		while(True):
			try:
				choice = int(input("({}{}{})> {}".format(Colors.green, info["name"], Colors.end, Colors.cyan)))
				print(Colors.end)
				break

			except Exception:
				print("{}{}".format(Icons.warn, reg.content["err"]["menuCho"]))

		for i in range(0, len(games)):
			if(choice == i+1):
				game = games[i](["admin", "root"], reg)
				print("{}{}".format(Icons.play, game.gameName))

				if(not game.finished):
					print("{}{}".format(Icons.warn, reg.content["game"]["notFinished"]))

				game.start()

		if(choice == 0):
			return(True)

		#elif(choice == len(menu)):
		#	print(" OPTION")

	return(True)

if __name__ == "__main__":
	games = [ ClosedBattle, Solitary, PeckerLady, Chickenshit, Liar ]
	info = {
		"name": "cardsGame.py",
		"vers": "0.1",
		"author": "Florian Cardinal"
	}

	try:
		with open("config.json") as outFile: # Importation du fichier de configuration
			cfg = json.load(outFile)
			reg = Regions(cfg["lang"])

	except Exception: # Paramétrage de la langue en anglais par défaut
		reg = Regions("us")
		print("{}{}".format(Icons.warn, reg.content["err"]["regLoad"]))
		print("{}{}".format(Icons.info, reg.content["tip"]["regLoad"]))

	if(len(argv) > 1):
		arg(cfg, reg, info, games)

	else:
		main(cfg, reg, info, games)
