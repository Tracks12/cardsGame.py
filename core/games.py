#!/bin/python3
# -*- coding: utf-8 -*-

# Module des types de jeux

from core.cards import Cards
from core.players import Players

class ClosedBattle(Cards, Players): # La bataille fermée
	gameName = "la bataille fermée"

	def __init__(self, player, playersName):
		Cards.__init__(self)
		Players.__init__(self)

		self.addPlayer(player, playersName)

class Solitary(Cards, Players): # Le solitaire
	gameName = "le solitaire"

	def __init__(self, playersName):
		Cards.__init__(self)
		Players.__init__(self)

		self.addPlayer(1, playersName)

class PeckerLady(Cards, Players): # La dame de pic
	gameName = "la dame de pic"

	def __init__(self, player, playersName):
		Cards.__init__(self)
		Players.__init__(self)

		self.addPlayer(player, playersName)

	def __rules(self):
		for player in self.players:
			if(player["score"] >= 100):
				self.end = True

		return True

	def start(self):
		print(self.players)

		return True

class Chickenshit(Cards, Players): # Le pouilleux ou mistigri
	gameName = "le pouilleux"

	def __init__(self, player, playersName):
		Cards.__init__(self)
		Players.__init__(self)

		self.addPlayer(player, playersName)

class Liar(Cards, Players): # Le menteur
	gameName = "le menteur"

	def __init__(self, player, playersName):
		Cards.__init__(self)
		Players.__init__(self)

		self.addPlayer(player, playersName)
