#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

class Players:
	def __init__(self, players):
		self._players = []

		self.__addPlayer(players)

	def __addPlayer(self, name): # Ajout d'un joueur
		for i in range(0, len(name)):
			self._players.append({
				"id":		len(self._players)+1,
				"name":		name[i],
				"score":	0,
				"deck": [],
				"hand":	[]
			})

		return self._players

	def getPlayers(self): # Affichage de la liste des joueurs
		return self._players

	def getPlayersById(self, plyrId): # Affichage d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["id"] == plyrId):
				return self._players[key]

	def getPlayersByName(self, plyrName): # Affichage d'un joueur par son nom
		for key, player in enumerate(self._players):
			if(player["name"] == plyrName):
				return self._players[key]

	def delPlayerById(self, plyrId): # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["id"] == plyrId):
				self._players.remove(player)

				return self._players

		return False

	def delPlayerByName(self, plyrName): # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["name"] == plyrName):
				self._players.remove(player)

				return self._players

		return False
