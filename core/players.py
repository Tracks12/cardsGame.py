#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

class Players:
	def __init__(self):
		self._players = []

	def getPlayers(self):
		return self._players

	def addPlayer(self, number, name): # Ajout d'un joueur
		for i in range(0, number):
			self._players.append({
				"id":		len(self._players)+1,
				"name":		name[i],
				"score":	0,
				"deck":		[]
			})

		return self._players

	def delPlayerByName(self, plyrName): # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["name"] == plyrName):
				self._players.remove(player)

				return self._players

		return False

	def delPlayerById(self, idPlyr): # Suppression d'un joueur par son id
		for key, player in enumerate(self._players):
			if(player["id"] == idPlyr):
				self._players.remove(player)

				return self._players

		return False
