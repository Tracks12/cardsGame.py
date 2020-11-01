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

		self.content	= lang.content["game"]["closedBattle"] # Traductions du jeu
		self.gameName	= self.content["name"]
		self.finished	= True # Jeu fini
		self.round		= 0 # Nombre de tour
		self.end		= False # État du jeu
		self.winner		= None # Vainqueur
		self.__table	= [] # Plateau
		self.__values	= [ # Valeurs des cartes du jeu
			("A", 14), ("K", 13), ("Q", 12), ("V", 11), ("10", 10), ("9", 9),
			("8", 8), ("7", 7), ("6", 6), ("5", 5), ("4", 4), ("3", 3), ("2", 2)
		]

	def __distrib(self): # Distribution des cartes
		spliting = int(len(self._packet)/len(self._players))

		for player in self._players:
			for i in range(0, spliting):
				player["hand"].append(self._packet[0])
				self._packet.pop(0)

	def __draw(self):
		for card in self.__table:
			self.getPlayerById(card[0])["deck"].append(card[1])

		self.__table = []

	def __update(self):
		max	= 0
		id	= 0

		for player in self._players:
			if(len(player["hand"]) == 0):
				for card in player["deck"]:
					player["hand"].append(card)
					player["hand"].reverse()

				player["deck"] = []

		for player in self._players:
			self.__table.append([player["id"], player["hand"][0]])
			player["hand"].pop(0)

		for card in self.__table:
			for value in self.__values:
				if((card[1][0] == value[0]) and (value[1] > max)):
					if(value[1] == max):
						self.__draw()
						return(True)

					max	= value[1]
					id	= card[0]

		for card in self.__table:
			self.getPlayerById(id)["deck"].append(card[1])

		self.__table = []

	def __rules(self): # Application des règles du jeu
		for player in self._players:
			if((len(player["hand"]) + len(player["deck"])) == 52):
				self.end	= True
				self.winner	= player

	def start(self): # Lancement de la partie
		self.mixCards()
		self.__distrib()

		while(not self.end):
			self.__update()
			self.__rules()
			self.round += 1

			print(" ----- {}: {} -----".format(self.content["round"], self.round))
			for player in self._players:
				print(" {}: {}".format(player["name"], (len(player["hand"]) + len(player["deck"]))))

		print("\n {} {}".format(self.winner["name"], self.content["winner"]))

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
		return(True)
