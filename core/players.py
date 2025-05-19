#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

from json import loads, dumps

from core import B64

class LoadPlayers:
	def __init__(self, encode: str):
		self.players	= list([])
		self.__encode	= str(encode)
		self.__path	= str("core/players")

		self.__loadJSON()

	def __loadJSON(self) -> None:
		try:
			with open(self.__path, "r", encoding=self.__encode) as outFile:
				self.players = list(loads(B64.decode(outFile.read())))

		except Exception:
			self.players = list([])

	def __saveJSON(self) -> bool:
		try:
			with open(self.__path, "w", encoding=self.__encode) as inFile:
				inFile.write(B64.encode(dumps(self.players)))

			return(True)

		except Exception:
			return(False)

	def insert(self, players: list) -> bool:
		self.players = list(players)

		return(self.__saveJSON())

class Players(LoadPlayers):
	def __init__(self, encode: str):
		LoadPlayers.__init__(self, str(encode))

		self._players = list([])

		self.__addPlayer(self.players)

	def __addPlayer(self, name) -> None: # Ajout d'un joueur
		for i in range(0, len(name)):
			self._players.append(dict({
				"id":			int(len(self._players)+1),
				"name":		str(name[i]),
				"score":	int(0),
				"deck":		list([]),
				"hand":		list([])
			}))

	def getPlayers(self) -> list: # Affichage de la liste des joueurs
		return(self._players)

	def getPlayerNames(self) -> list: # Affichage de la liste des joueurs
		playerList = list([])
		for player in self._players:
			playerList.append(player["name"])

		return(playerList)

	def getPlayerById(self, plyrId: int) -> dict: # Affichage d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["id"] == int(plyrId)):
				return(self._players[key])

	def getPlayerByName(self, plyrName: str) -> dict: # Affichage d'un joueur par son nom
		for key, player in enumerate(self._players):
			if(player["name"] == str(plyrName)):
				return(self._players[key])

	def delPlayerById(self, plyrId: int) -> bool: # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["id"] == int(plyrId)):
				self._players.remove(player)

				return(True)

		return(False)

	def delPlayerByName(self, plyrName: str) -> bool: # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["name"] == str(plyrName)):
				self._players.remove(player)

				return(True)

		return(False)
