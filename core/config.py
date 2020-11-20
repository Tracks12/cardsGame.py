#!/bin/python3
# -*- coding: utf-8 -*-

# Module d'affichage des textes par langue

from json import dump, load
from os import listdir

from core import Icons

class Config:
	def __init__(self):
		self.__config	= {}
		self.__encode	= "utf-8"
		self.__path		= "config.json"
		self.encoding 	= self.__encode	# Encodage par défaut
		self.language	= "us"			# Langue par défaut
		self.splash		= True			# Screen de bienvenu par défaut

		self.loaded		= self.__loadJSON()

	def __loadJSON(self): # Importation du fichier de configuration
		try:
			with open(self.__path, "r", encoding=self.__encode) as outFile:
				self.__config	= load(outFile)
				self.encoding 	= self.__config["encoding"]
				self.language	= self.__config["language"]
				self.splash		= self.__config["splash"]

		except Exception:
			print("{}No config file found".format(Icons.warn))
			return(False)

		return(True)

	def __saveJSON(self): # Sauvearde du fichier de configuration
		try:
			with open(self.__path, "w", encoding=self.__encode) as inFile:
				self.__config = {
					"encoding": self.encoding,
					"language": self.language,
					"splash": self.splash
				}

				dump(self.__config, inFile, sort_keys=True, indent=2)

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
