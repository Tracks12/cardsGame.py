#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

import json
from core.icons import Icons

class Regions:
	def __init__(self, lang): # Selection de la langue dans le constructeur
		self.content	= {}
		self.__path		= "core/regions/"

		self.__loadJSON(lang)

	def __loadJSON(self, lang): # Chargement des langues depuis un fichier
		try:
			with open("{}{}.json".format(self.__path, lang), encoding="utf-8") as outFile:
				self.content = json.load(outFile)

		except Exception: # Chargement du contenu de langue anglais par défaut
			self.content = {
				"args": {
					"intro": ["Card games", "Launch", "Arguments"],
					"desc": [
						"\tDisplays a packet card",
						"\tDisplays the entire packet of cards",
						"Displays a mixed packet card",
						"\tDisplays all cards of the shuffled packet",
						"\tLaunch a card game\n",
						"\t\tDisplays the help menu",
						"\t\tDebug mode",
						"\t\tDisplays the version of the program\n"
					]
				},
				"debug": {
					"continue": "Press key to continue ..."
				},
				"err": {
					"regLoad": "The loading of the language module failed",
					"menuCho": "This choice does not exist",
					"cardNum": "Specify a card number",
					"gameName": "Enter a game name"
				},
				"tip": {
					"regLoad": "Check the 'regions.json' file is complete"
				},
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

			print("{}{}".format(Icons.warn, self.content["err"]["regLoad"]))
			print("{}{}".format(Icons.info, self.content["tip"]["regLoad"]))
