#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

from json import loads, dumps
from os.path import abspath, dirname

from core import B64
from core.cards import Card

class Player:
	def __init__(self, props: dict):
		self.id		: int			= int(props["id"])
		self.name	: str			= str(props["name"])
		self.score	: int			= int(props["score"])
		self.deck	: list[Card]	= list[Card](props["deck"])
		self.hand	: list[Card]	= list[Card](props["hand"])

class LoadPlayers:
	def __init__(self, encode: str):
		self.players	: list[str]	= list[str]([])
		self.__encode	: str		= str(encode)
		self.__path		: str		= str(f"{dirname(abspath(__file__))}/players")

		self.__loadJSON()

	def __loadJSON(self) -> None:
		try:
			with open(self.__path, "r", encoding=self.__encode) as outFile:
				self.players = list[str](loads(B64.decode(outFile.read())))

		except(Exception):
			self.players = list[str]([])

	def __saveJSON(self) -> bool:
		try:
			with open(self.__path, "w", encoding=self.__encode) as inFile:
				inFile.write(B64.encode(dumps(self.players)))

			return(True)

		except(Exception):
			return(False)

	def insert(self, players: list[str]) -> bool:
		self.players = list[str](players)

		return(self.__saveJSON())

class Players(LoadPlayers):
	def __init__(self, encode: str):
		LoadPlayers.__init__(self, str(encode))

		self._players	: list[Player]	= list[Player]([])

		self.__addPlayer(self.players)

	def __addPlayer(self, names: list[str]) -> None: # Ajout d'un joueur
		for name in names:
			self._players.append(Player({
				"id"	: int(len(self._players)+1),
				"name"	: str(name),
				"score"	: int(0),
				"deck"	: list[tuple]([]),
				"hand"	: list[tuple]([])
			}))

	def getPlayers(self) -> list[Player]: # Affichage de la liste des joueurs
		return(self._players)

	def getPlayerNames(self) -> list[str]: # Affichage de la liste des joueurs
		playerList = list[str]([])
		for player in self._players:
			playerList.append(player.name)

		return(playerList)

	def getPlayerById(self, plyrId: int) -> Player: # Affichage d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player.id == int(plyrId)):
				return(self._players[key])

	def getPlayerByName(self, plyrName: str) -> Player: # Affichage d'un joueur par son nom
		for key, player in enumerate(self._players):
			if(player.name == str(plyrName)):
				return(self._players[key])

	def delPlayerById(self, plyrId: int) -> bool: # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player.id == int(plyrId)):
				self._players.remove(player)
				self.players.remove(player.name)

				return(True)

		return(False)

	def delPlayerByName(self, plyrName: str) -> bool: # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player.name == str(plyrName)):
				self._players.remove(player)
				self.players.remove(player.name)

				return(True)

		return(False)
