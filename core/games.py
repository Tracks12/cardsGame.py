#!/bin/python3
# -*- coding: utf-8 -*-

# Module des types de jeux

from core.cards import Cards
from core.players import Players

class ClosedBattle(Cards, Players): # La bataille fermée
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["closedBattle"]
		self.gameName	= self.content["name"]
		self.end		= False

class Solitary(Cards, Players): # Le solitaire
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["solitary"]
		self.gameName	= self.content["name"]
		self.end		= False

class PeckerLady(Cards, Players): # La dame de pic
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["peckerLady"]
		self.gameName	= self.content["name"]
		self.end		= False

	def __rules(self):
		for player in self.players:
			if(player["score"] >= 100):
				self.end = True

		return True

	def start(self):
		self.mixCards()

		print(self.gameName)

		return True

class Chickenshit(Cards, Players): # Le pouilleux ou mistigri
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["chickenshit"]
		self.gameName	= self.content["name"]
		self.end		= False

class Liar(Cards, Players): # Le menteur
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["liar"]
		self.gameName	= self.content["name"]
		self.end		= False
