#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

from json import loads, dumps

from core import B64

class LoadPlayers:
	def __init__(self, encode):
		self.players	= []
		self.__encode	= encode
		self.__path		= "core/players"

		self.__loadJSON()

	def __loadJSON(self):
		try:
			with open(self.__path, "r", encoding=self.__encode) as outFile:
				self.players = loads(B64.decode(outFile.read()))

		except Exception:
			self.players = []

	def __saveJSON(self):
		try:
			with open(self.__path, "w", encoding=self.__encode) as inFile:
				inFile.write(B64.encode(dumps(self.players)))

			return(True)

		except Exception:
			return(False)

	def insert(self, players):
		self.players = players

		return(self.__saveJSON())

class Players(LoadPlayers):
	def __init__(self, encode):
		LoadPlayers.__init__(self, encode)

		self._players = []

		self.__addPlayer(self.players)

	def __addPlayer(self, name): # Ajout d'un joueur
		for i in range(0, len(name)):
			self._players.append({
				"id":		len(self._players)+1,
				"name":		name[i],
				"score":	0,
				"deck":		[],
				"hand":		[]
			})

	def getPlayers(self): # Affichage de la liste des joueurs
		return self._players

	def getPlayerById(self, plyrId): # Affichage d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["id"] == plyrId):
				return self._players[key]

	def getPlayerByName(self, plyrName): # Affichage d'un joueur par son nom
		for key, player in enumerate(self._players):
			if(player["name"] == plyrName):
				return self._players[key]

	def delPlayerById(self, plyrId): # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["id"] == plyrId):
				self._players.remove(player)

				return(True)

		return(False)

	def delPlayerByName(self, plyrName): # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["name"] == plyrName):
				self._players.remove(player)

				return(True)

		return(False)
