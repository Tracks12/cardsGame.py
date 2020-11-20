#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

from json import dump, load
from os import listdir

from core import Icons

class Config:
	def __init__(self):
		self.__config	= dict({})
		self.__encode	= str("utf-8")
		self.__path		= str("config.json")
		self.encoding 	= str(self.__encode)	# Encodage par défaut
		self.language	= str("us")				# Langue par défaut
		self.splash		= bool(True)			# Screen de bienvenu par défaut

		self.loaded		= bool(self.__loadJSON())

	def __loadJSON(self): # Importation du fichier de configuration
		try:
			with open(self.__path, "r", encoding=self.__encode) as outFile:
				self.__config	= dict(load(outFile))
				self.encoding 	= str(self.__config["encoding"])
				self.language	= str(self.__config["language"])
				self.splash		= bool(self.__config["splash"])

		except Exception:
			print("{}No config file found".format(Icons.warn))
			return(False)

		return(True)

	def __saveJSON(self): # Sauvearde du fichier de configuration
		try:
			with open(self.__path, "w", encoding=self.__encode) as inFile:
				self.__config = dict({
					"encoding": str(self.encoding),
					"language": str(self.language),
					"splash": bool(self.splash)
				})

				dump(dict(self.__config), inFile, sort_keys=True, indent=2)

		except Exception:
			print("{}No config file found".format(Icons.warn))
			return(False)

		return(True)

	def setEncode(self, coding = "utf-8"): # Encodage setter
		if(coding.lower() in ("ascii", "utf-8", "utf-16", "utf-32")):
			self.encoding = str(coding.lower())
			self.__saveJSON()

			return(True)

		return(False)

	def setLanguage(self, lang = "us"): # Langage setter
		langs	= listdir("core/regions")
		for k, v in enumerate(langs):
			langs[k] = v.split(".")[0]

		if(lang.lower() in langs):
			self.language = str(lang.lower())
			self.__saveJSON()

			return(True)

		return(False)

	def setSplash(self, splash = True): # Splash setter
		self.splash = bool(splash in ("True", "true"))
		self.__saveJSON()

		return(True)
