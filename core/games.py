#!/bin/python3
# -*- coding: utf-8 -*-

# Module des types de jeux

from time import sleep
from core.cards import Cards
from core.players import Players

class ClosedBattle(Cards, Players): # La bataille fermée
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["closedBattle"]
		self.gameName	= self.content["name"]
		self.finished	= False
		self.end		= False

	def __distrib(self):
		spliting = int(len(self._packet)/len(self._players))

		for player in self._players:
			for i in range(0, spliting):
				player["hand"].append(self._packet[0])
				self._packet.pop(0)

	def __update(self):


		return(True)

	def __rules(self):
		for player in self._players:
			if(len(player["hand"]) == 52):
				self.end = True

	def start(self):
		print(self.gameName)

		self.mixCards()
		self.__distrib()

		while(not self.end):
			self.__update()
			self.__rules()

			print(self.getPlayers())
			sleep(.25)

		return(True)

class Solitary(Cards, Players): # Le solitaire
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["solitary"]
		self.gameName	= self.content["name"]
		self.finished	= False
		self.end		= False

	def start(self):
		print(self.gameName)

		return(True)

class PeckerLady(Cards, Players): # La dame de pic
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["peckerLady"]
		self.gameName	= self.content["name"]
		self.finished	= False
		self.end		= False

	def __rules(self):
		for player in self.players:
			if(player["score"] >= 100):
				self.end = True

	def start(self):
		print(self.gameName)

		return(True)

class Chickenshit(Cards, Players): # Le pouilleux ou mistigri
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["chickenshit"]
		self.gameName	= self.content["name"]
		self.finished	= False
		self.end		= False

	def start(self):
		print(self.gameName)

		return(True)

class Liar(Cards, Players): # Le menteur
	def __init__(self, players, lang):
		Cards.__init__(self)
		Players.__init__(self, players)

		self.content	= lang.content["game"]["liar"]
		self.gameName	= self.content["name"]
		self.finished	= False
		self.end		= False

	def start(self):
		print(self.gameName)

		return(True)
