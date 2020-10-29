#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

class Players:
	def __init__(self):
		self.players = []

	def addPlayer(self, number): # Ajout d'un joueur
		for i in range(0, number):
			self.players.append({
				"id":		len(self.players)+1,
				"score":	0,
				"deck":		[]
			})

		return self.players

	def delPlayer(self, idPlyr): # Suppression d'un joueur par son id
		for key, player in enumerate(self.players):
			if(player["id"] == idPlyr):
				self.players.remove(player)

				return self.players

		return False
