#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

class Players:
	def __init__(self):
		self.players = []

	def addPlayer(self, number, name): # Ajout d'un joueur
		for i in range(0, number):
			self.players.append({
				"id":		len(self.players)+1,
				"name":		name[i],
				"score":	0,
				"deck":		[]
			})

		return self.players

	def delPlayerByName(self, plyrName): # Suppression d'un joueur par son id
		for key, player in enumerate(self.players):
			if(player["name"] == plyrName):
				self.players.remove(player)

				return self.players

		return False

	def delPlayerById(self, idPlyr): # Suppression d'un joueur par son id
		for key, player in enumerate(self.players):
			if(player["id"] == idPlyr):
				self.players.remove(player)

				return self.players

		return False
