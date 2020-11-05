#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

from json import load
from core.icons import Icons

class Config:
	def __init__(self):
		self.config		= {}
		self.__encode	= "utf-8"
		self.__path		= "config.json"

		self.__loadJSON()

	def __loadJSON(self): # Importation du fichier de configuration
		try:
			with open(self.__path, encoding=self.__encode) as outFile:
				self.config = load(outFile)

		except Exception: # Création d'une configuration par défaut
			self.config = {
				"encoding": self.__encode,
				"language": "us",
				"splash": True
			}

			print("{}No config file found".format(Icons.warn))
