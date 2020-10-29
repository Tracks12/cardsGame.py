#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets joueurs

class Players:
	def __init__(self):
		self.players = []

	def addPlayer(self, number):
		for i in range(0, number):
			self.players.append({
				"score": 0,
				"deck": []
			})

		return self.players
