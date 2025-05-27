#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

from json import load
from os.path import abspath, dirname

from core import Icons

class Regions:
	def __init__(self, lang: str, encode: str): # Selection de la langue dans le constructeur
		self.content	= dict({})
		self.__encode	= str(encode)
		self.__lang		= str(lang)
		self.__path		= str(f"{dirname(abspath(__file__))}/regions/")

		self.__loadJSON()

	def __loadJSON(self) -> bool: # Chargement des langues depuis un fichier
		try:
			with open(f"{self.__path}{self.__lang}.json", "r", encoding=self.__encode) as outFile:
				self.content = dict(load(outFile))

				if(self.content == {}):
					raise(Exception(f'No translations in "{self.__lang}.json"'))

				return(True)

		except Exception: # Création du contenu de langue anglais par défaut
			self.content = dict({
				"ARGS_DESC": [
					"Displays a card from the deck",
					"Displays the entire deck",
					"Displays a card from the shuffled deck",
					"Displays all cards in the shuffled deck",
					"Launches a card game",
					"Insert one or more players",
					"Displays the list of games and players",
					"Displays the help menu",
					"Debugger mode",
					"Displays the program version"
				],
				"ARGS_INTRO": [
					"Cards games",
					"Launch",
					"Arguments"
				],
				"COMMON_BACK": "return",
				"COMMON_BY": "by",
				"COMMON_GAMES": "Games",
				"COMMON_NAME": "Name",
				"COMMON_NO": "No",
				"COMMON_PATH": "Path",
				"COMMON_PLAYABLE": "Playable",
				"COMMON_PLAYER": "The player",
				"COMMON_PLAYERS": "Players",
				"COMMON_UNPLAYABLE": "Not playable",
				"COMMON_YES": "Yes",
				"DEBUG_CONTINUE": "Press any key to continue...",
				"DEBUG_STARTING": "Launching in debugger mode",
				"ERR_ARGS": "Unknown arguments",
				"ERR_CARD_NUMBER": "Specify a card number",
				"ERR_GAME_NAME": "Enter a game name",
				"ERR_LIST": "Unknown list type",
				"ERR_MENU_CHOICE": "This choice does not exist",
				"ERR_PLAYER_EXIST": "Player does not exist",
				"ERR_PLAYER_LIST": "The player list is incorrect",
				"GAME_CHICKENSHIT": {
					"_NAME": "The Lousy One"
				},
				"GAME_CLOSEDBATTLE": {
					"_NAME": "Closed Battle",
					"_ROUND": "Round",
					"_WINNER": "is winner"
				},
				"GAME_HEIGHTAMERICAN": {
					"_NAME": "An 8 American"
				},
				"GAME_LIAR": {
					"_NAME": "The Liar"
				},
				"GAME_NOTFINISHED": "This game is not finished",
				"GAME_PECKERLADY": {
					"_NAME": "The Queen of Spades"
				},
				"GAME_SOLITARY": {
					"_NAME": "Solitaire"
				},
				"MENU_CHOICE_PLAYER": "Players",
				"MENU_CHOICE_QUIT": "Quit",
				"MENU_CHOICE_SETTINGS": "Settings",
				"MENU_CONFIG_CONTENT_ENCODING": "Encoding",
				"MENU_CONFIG_CONTENT_LANGUAGE": "Language",
				"MENU_CONFIG_CONTENT_SPLASH": "Splash screen",
				"MENU_CONFIG_FAIL": "Configuration not applied",
				"MENU_CONFIG_LABEL": "settings",
				"MENU_CONFIG_RESTART": "Restart the program to apply the new configuration",
				"MENU_CONFIG_SUCCESS": "Configuration applied",
				"MENU_PLAYER_CONTENT_ADD": "Add a player",
				"MENU_PLAYER_CONTENT_LIST": "Show player list",
				"MENU_PLAYER_CONTENT_REMOVE": "Delete a player",
				"MENU_PLAYER_INPUT_NAME": "New player name",
				"MENU_PLAYER_INPUT_NUMBER": "Player number to delete",
				"MENU_PLAYER_LABEL": "players",
				"MENU_PLAYER_RESULT_ADDED": "has been added",
				"MENU_PLAYER_RESULT_DELETED": "has been deleted",
				"MENU_TEXT": "Choose a game mode"
			})

			print(f"{Icons.warn}The loading of the language module failed")
			print(f'{Icons.info}Check the "config.json" or if the language file is complete in "core/regions/"')

		return(False)
