#!/bin/python3
# -*- coding: utf-8 -*-

# Module des types de jeux

from core.cards import Cards
from core.players import Players

class ClosedBattle(Cards, Players): # La bataille fermée
	def __init__(self, player, playersName):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.gameName	= "la bataille fermée"
		self.end		= False

class Solitary(Cards, Players): # Le solitaire
	def __init__(self, playersName):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.gameName	= "le solitaire"
		self.end		= False

class PeckerLady(Cards, Players): # La dame de pic
	def __init__(self, players):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.gameName	= "la dame de pic"
		self.end		= False

	def __rules(self):
		for player in self.players:
			if(player["score"] >= 100):
				self.end = True

		return True

	def start(self):
		self.mixCards()

		print(self.getPlayers())
		print(self.getAllCards())

		return True

class Chickenshit(Cards, Players): # Le pouilleux ou mistigri
	def __init__(self, player, playersName):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.gameName	= "le pouilleux"
		self.end		= False

class Liar(Cards, Players): # Le menteur
	def __init__(self, player, playersName):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.gameName	= "le menteur"
		self.end		= False
