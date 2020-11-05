#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

import json
from core.icons import Icons

class Regions:
	def __init__(self, lang, encode): # Selection de la langue dans le constructeur
		self.content	= {}
		self.__encode	= encode
		self.__lang		= lang
		self.__path		= "core/regions/"

		self.__loadJSON()

	def __loadJSON(self): # Chargement des langues depuis un fichier
		try:
			with open("{}{}.json".format(self.__path, self.__lang), encoding=self.__encode) as outFile:
				self.content = json.load(outFile)

		except Exception: # Création du contenu de langue anglais par défaut
			self.content = {
				"args": {
					"intro": ["Card games", "Launch", "Arguments"],
					"desc": [
						"\tDisplays a packet card",
						"\tDisplays the entire packet of cards",
						"Displays a mixed packet card",
						"\tDisplays all cards of the shuffled packet\n",
						"\tLaunch a card game",
						"Insert one or more player(s)\n",
						"\t\tDisplays the help menu",
						"\t\tDebug mode",
						"\t\tDisplays the version of the program\n"
					]
				},
				"debug": {
					"continue": "Press key to continue ..."
				},
				"err": {
					"menuCho": "This choice does not exist",
					"cardNum": "Specify a card number",
					"gameName": "Enter a game name",
					"player": "Player list is incorrect"
				},
				"tip": {},
				"menu": {
					"txt": "Choose a game mode",
					"quit": "Quit",
					"set": "Settings"
				},
				"game": {
					"closedBattle": {
						"name": "The Closed Battle",
						"round": "Round",
						"winner": "is the Winner"
					},
					"solitary": {
						"name": "The Solitary"
					},
					"peckerLady": {
						"name": "The Pecker Lady"
					},
					"chickenshit": {
						"name": "The Chickenshit"
					},
					"liar": {
						"name": "The Liar"
					},
					"notFinished": "This game wasn't finished"
				},
				"vers": "by"
			}

			print("{}The loading of the language module failed".format(Icons.warn))
			print("{}Check the language file is complete in \"core/regions/\"".format(Icons.info))
