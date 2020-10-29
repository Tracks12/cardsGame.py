#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

import json

class Regions:
	def __init__(self, lang): # Selection de la langue dans le constructeur
		self.content	= {}
		self.__path		= "regions.json"

		self.__loadJSON()

		self.content = self.content[lang]

	def __loadJSON(self): # Chargement des langues depuis un fichier
		try:
			with open(self.__path) as outFile:
				self.content = json.load(outFile)

			return True

		except Exception:
			return False
