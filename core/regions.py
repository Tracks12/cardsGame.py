#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

from json import load

from core import Icons

class Regions:
	def __init__(self, lang, encode): # Selection de la langue dans le constructeur
		self.content	= dict({})
		self.__encode	= str(encode)
		self.__lang		= str(lang)
		self.__path		= str("core/regions/")

		self.__loadJSON()

	def __loadJSON(self): # Chargement des langues depuis un fichier
		try:
			with open(f"{self.__path}{self.__lang}.json", "r", encoding=self.__encode) as outFile:
				self.content = dict(load(outFile))

		except Exception: # Création du contenu de langue anglais par défaut
			self.content = {
				"args": {
					"intro": ["Card games", "Launch", "Arguments"],
					"desc": [
						"Displays a packet card",
						"Displays the entire packet of cards",
						"Displays a mixed packet card",
						"Displays all cards of the shuffled packet",
						"Launch a card game",
						"Insert one or more player(s)",
						"Displays the help menu",
						"Debug mode",
						"Displays the version of the program"
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
					"config": {
						"content": {
							"encoding": "Encoding",
							"language": "Language",
							"splash": "Splash screen"
						},
						"label": "settings",
						"back": "back",
						"success": "Config applied",
						"failed": "Config not applied",
						"restart": "Restart program to apply the new config"
					},
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

			print(f"{Icons.warn}The loading of the language module failed")
			print(f'{Icons.info}Check the language file is complete in "core/regions/"')
