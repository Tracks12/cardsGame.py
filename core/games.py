#!/bin/python3
# -*- coding: utf-8 -*-

# Module des types de jeux

from core import Colors
from core.cards import Cards
from core.players import Players

class ClosedBattle(Cards, Players): # La bataille fermée
	def __init__(self, lang, encode):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.content	= dict(lang["game"]["closedBattle"]) # Traductions du jeu
		self.gameName	= str(self.content["name"]) # Nom du jeu
		self.finished	= bool(True) # Jeu fini
		self.__end		= bool(False) # État du jeu
		self.__round	= int(0) # Nombre de tour
		self.__table	= list([]) # Plateau
		self.__winner	= None # Vainqueur
		self.__values	= tuple(( # Valeurs des cartes du jeu
			("A", 14), ("K", 13), ("Q", 12), ("V", 11), ("10", 10), ("9", 9),
			("8", 8), ("7", 7), ("6", 6), ("5", 5), ("4", 4), ("3", 3), ("2", 2)
		))

	def __clearTable(self): # Vide le plateau
		self.__table = list([])

	def __dispCardOnTable(self): # Affichage des cartes joueurs
		screen = list([])
		for i in range(0, 6):
			screen.append("")

		for card in self.__table:
			color = str(Colors.red if(card[1][1] in ("♥", "♦")) else Colors.cyan)
			plyrName = self.getPlayerById(card[0])['name']
			spacing = 8

			screen[0] += f",-----,{' '*spacing}"
			screen[1] += f"|{color}{card[1][0]}{' ' if(len(card[1][0]) < 2) else ''}{Colors.end}   |{' '*spacing}"
			screen[2] += f"|  {color}{card[1][1]}{Colors.end}  |{' '*spacing}"
			screen[3] += f"|   {color}{' ' if(len(card[1][0]) < 2) else ''}{card[1][0]}{Colors.end}|{' '*spacing}"
			screen[4] += f"`-----`{' '*spacing}"
			screen[5] += f" {self.getPlayerById(card[0])['name']}{' '*(spacing-(len(self.getPlayerById(card[0])['name'])-5)+1)}"

		for line in screen:
			print(line)

	def __distrib(self): # Distribution des cartes
		spliting = int(len(self._packet)/len(self._players))

		for player in self._players:
			for i in range(0, spliting):
				player["hand"].append(self._packet[0])
				self._packet.pop(0)

	def __draw(self):
		for card in self.__table:
			self.getPlayerById(card[0])["deck"].append(card[1])

		self.__clearTable()

	def __update(self): # Mise à jour du jeu
		max	= int(0)
		id	= int(0)

		for player in self._players:
			if(len(player["hand"]) == 0):
				for card in player["deck"]:
					player["hand"].append(card)
					player["hand"].reverse()

				player["deck"] = list([])

		for player in self._players:
			self.__table.append([player["id"], player["hand"][0]])
			player["hand"].pop(0)

		for card in self.__table:
			for value in self.__values:
				if((card[1][0] == value[0]) and (value[1] > max)):
					if(value[1] == max):
						self.__draw()
						return(True)

					max	= int(value[1])
					id	= int(card[0])

		for card in self.__table:
			self.getPlayerById(id)["deck"].append(card[1])

	def __rules(self): # Application des règles du jeu
		for player in self._players:
			if((len(player["hand"]) + len(player["deck"])) == 52):
				self.__end		= bool(True)
				self.__winner	= dict(player)

	def start(self): # Lancement de la partie
		self.mixCards()
		self.__distrib()

		while(not self.__end):
			print(f" ----- {self.content['round']}: {self.__round} -----")
			self.__update()
			self.__dispCardOnTable()
			self.__clearTable()
			self.__rules()
			self.__round += 1

			print("")
			for player in self._players:
				print(f" {player['name']}: {len(player['hand']) + len(player['deck'])}")

			print("")

		print(f" {self.__winner['name']} {self.content['winner']} !")

		return(True)

class Solitary(Cards, Players): # Le solitaire
	def __init__(self, lang, encode):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.content	= dict(lang["game"]["solitary"])
		self.gameName	= str(self.content["name"])
		self.finished	= bool(False)
		self.__end		= bool(False)
		self.__table	= list([])

	def __update(self):
		self.__end = bool(True)

	def start(self):
		while(not self.__end):
			self.__update()

		return(True)

class PeckerLady(Cards, Players): # La dame de pic
	def __init__(self, lang, encode):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.content	= dict(lang["game"]["peckerLady"])
		self.gameName	= str(self.content["name"])
		self.finished	= bool(False)
		self.__end		= bool(False)
		self.__round	= int(0)
		self.__table	= list([])
		self.__winner	= None

	def __update(self):
		self.__end = bool(True)

	def __rules(self):
		for player in self.players:
			if(player["score"] >= 100):
				self.end = bool(True)

	def start(self):
		while(not self.__end):
			self.__update()

		return(True)

class Chickenshit(Cards, Players): # Le pouilleux ou mistigri
	def __init__(self, lang, encode):
		Cards.__init__(self, 1)
		Players.__init__(self, str(encode))

		self.content	= dict(lang["game"]["chickenshit"])
		self.gameName	= str(self.content["name"])
		self.finished	= bool(False)
		self.__end		= bool(False)
		self.__round	= int(0)
		self.__table	= list([])
		self.__winner	= None

	def __update(self):
		self.__end = bool(True)

	def start(self):
		while(not self.__end):
			self.__update()

		return(True)

class Liar(Cards, Players): # Le menteur
	def __init__(self, lang, encode):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.content	= dict(lang["game"]["liar"])
		self.gameName	= str(self.content["name"])
		self.finished	= bool(False)
		self.__end		= bool(False)
		self.__round	= int(0)
		self.__table	= list([])
		self.__winner	= None

	def __update(self):
		self.__end = bool(True)

	def start(self):
		while(not self.__end):
			self.__update()

		return(True)
