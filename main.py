#!/bin/python3
# -*- coding: utf-8 -*-

from os import system as shell
from platform import system
from sys import argv

# Importation des dépendances internes
from core import Colors, Icons, splash
from core.config import Config
from core.regions import Regions
from core.players import LoadPlayers
from core.cards import Cards
from core.games import *

def arg(cfg, reg, info, games): # Fonction d'entrée des arguments
	args = {
		"prfx": (
			(("-s", "--show-card"), "<x>"),
			(("-S", "--show-all"), ""),
			(("-r", "--show-rand-card"), "<x>"),
			(("-R", "--show-rand-all"), ""),
			(("-g", "--game"), "<gameName>"),
			(("-p", "--players"), "\"['name', ...]\""),
			(("-h", "--help"), ""),
			(("-d", "--debug"), ""),
			(("-v", "--version"), "")
		),
		"desc": reg["args"]["desc"]
	}

	if(argv[1] in args["prfx"][-3][0]): # Affiche le helper args
		print(" {}".format(reg["args"]["intro"][0]))
		print(" {}: python main.py <arg>\n".format(reg["args"]["intro"][1]))
		print(" {}:".format(reg["args"]["intro"][2]))

		for i in range(0, len(args["prfx"])):
			print(" {}, {} {}\t{}".format(args["prfx"][i][0][0], args["prfx"][i][0][1], args["prfx"][i][1], args["desc"][i]))

	elif(argv[1] in args["prfx"][-2][0]): # Mode Debugger
		isLinux = True if(system() == "Linux") else False

		while(True):
			shell("clear" if(isLinux) else "cls")
			shell("python{} main.py".format("3" if(isLinux) else ""))
			input("{}{}".format(Icons.info, reg["debug"]["continue"]))

	elif(argv[1] in args["prfx"][-1][0]): # Affiche la version du script
		print(" {} {} {} {}\n".format(info["name"], info["vers"], reg["vers"], info["author"]))

	elif(argv[1] in args["prfx"][0][0]): # Affiche une carte du paquet
		packets = Cards(2)

		try:
			card = int(argv[2])-1

		except Exception:
			print("{}{}".format(Icons.warn, reg["err"]["cardNum"]))

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
			print("{}{}".format(Icons.warn, reg["err"]["cardNum"]))

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
			print("{}{}".format(Icons.warn, reg["err"]["gameName"]))

			return(False)

		gameList = []
		for game in games:
			gameList.append(game(reg, cfg["encoding"]).gameName)

		for id, name in enumerate(gameList):
			if(gameName == name):
				game = games[id](reg, cfg["encoding"])
				print("{}{}".format(Icons.play, game.gameName))

				if(not game.finished):
					print("{}{}".format(Icons.warn, reg["game"]["notFinished"]))

				game.start()

	elif(argv[1] in args["prfx"][5][0]): # Gestion des joueurs
		try:
			playersList = list(eval(argv[2]))

		except Exception:
			print("{}{}".format(Icons.warn, reg["err"]["player"]))

			return(False)

		players	= LoadPlayers(cfg["encoding"])
		players.insert(playersList)

	return(True)

def main(cfg, reg, info, games): # Fonction principale de l'execution du programme
	if(cfg["splash"]):
		splash(reg, info)

	menu = [ "{}:\n".format(reg["menu"]["txt"]) ]
	for game in games:
		menu.append(game(reg, cfg["encoding"]).gameName)

	for key, row in enumerate(menu):
		print(" {}{}".format("" if(key == 0) else "{}{}.{} ".format(Colors.cyan, key, Colors.end), row))

	print("")
	#print( " {}{}.{} {}".format(Colors.yellow, len(menu), Colors.end, reg["menu"]["set"]))
	print( " {}0.{} {}\n".format(Colors.red, Colors.end, reg["menu"]["quit"]))

	while(True):
		while(True):
			try:
				choice = int(input("({}{}{})> {}".format(Colors.green, info["name"], Colors.end, Colors.cyan)))
				print(Colors.end)
				break

			except Exception:
				print("{}{}".format(Icons.warn, reg["err"]["menuCho"]))

		for i in range(0, len(games)):
			if(choice == i+1):
				game = games[i](reg, cfg["encoding"])
				print("{}{}".format(Icons.play, game.gameName))

				if(not game.finished):
					print("{}{}".format(Icons.warn, reg["game"]["notFinished"]))

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

	cfg = Config().config # Chargement du fichier de configuration
	reg = Regions(cfg["language"], cfg["encoding"]).content # Chargement de la langue

	if(len(argv) > 1):
		arg(cfg, reg, info, games)

	else:
		main(cfg, reg, info, games)
