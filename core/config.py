#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

import json
from core.icons import Icons

class Config:
	def __init__(self):
		self.config	= {}
		self.__path	= "config.json"

		self.__loadJSON()

	def __loadJSON(self): # Importation du fichier de configuration
		try:
			with open(self.__path, encoding="utf-8") as outFile:
				self.config = json.load(outFile)

		except Exception: # Création d'une configuration par défaut
			self.config = {
				"encoding": "utf-8",
				"language": "us",
				"splash": True
			}

			print("{}No config file found".format(Icons.warn))
