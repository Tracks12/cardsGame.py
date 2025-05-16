#!/bin/python3
# -*- coding: utf-8 -*-

from core import Colors
from core.cards import Cards
from core.players import Players

class ClosedBattle(Cards, Players): # La bataille fermée
	def __init__(self, lang, encode):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.__file__ = __file__
		self.content	= dict(lang["GAME_CLOSEDBATTLE"]) # Traductions du jeu
		self.gameName	= str(self.content["_NAME"]) # Nom du jeu
		self.finished	= bool(True) # Jeu fini
		self.__end		= bool(False) # État du jeu
		self.__round	= int(0) # Nombre de tour
		self.__table	= list([]) # Plateau
		self.__winner	= None # Vainqueur
		self.__values	= tuple(( # Valeurs des cartes du jeu
			("A", 14), ("K", 13), ("Q", 12), ("V", 11), ("10", 10), ("9", 9),
			("8", 8), ("7", 7), ("6", 6), ("5", 5), ("4", 4), ("3", 3), ("2", 2)
		))

	def __clearTable(self) -> None: # Vide le plateau
		self.__table = list([])

	def __displayCardOnTable(self) -> None: # Affichage des cartes joueurs
		screen = list([])
		for i in range(0, 6):
			screen.append("")

		for i, card in enumerate(self.__table):
			color = str(Colors.red if(card[1][1] in ("♥", "♦")) else Colors.cyan)
			space = f"{' ' if(not i) else ' '*9}"

			screen[0] += f"{space},-----,"
			screen[1] += f"{space}|{color}{card[1][0]}{' ' if(len(card[1][0]) < 2) else ''}{Colors.end}   |"
			screen[2] += f"{space}|  {color}{card[1][1]}{Colors.end}  |"
			screen[3] += f"{space}|   {color}{' ' if(len(card[1][0]) < 2) else ''}{card[1][0]}{Colors.end}|"
			screen[4] += f"{space}`-----`"
			screen[5] += f"{space}{self.getPlayerById(card[0])['name']}{' '*(7-len(self.getPlayerById(card[0])['name']))}"

		for line in screen:
			print(line)

	def __distrib(self) -> None: # Distribution des cartes
		spliting = int(len(self._packet)/len(self.getPlayers()))

		for player in self.getPlayers():
			for i in range(0, spliting):
				player["hand"].append(self._packet[0])
				self._packet.pop(0)

	def __draw(self) -> None:
		for card in self.__table:
			self.getPlayerById(card[0])["deck"].append(card[1])

		self.__clearTable()

	def __update(self) -> None: # Mise à jour du jeu
		max	= int(0)
		id	= int(0)

		for player in self.getPlayers():
			if(len(player["hand"]) == 0):
				for card in player["deck"]:
					player["hand"].append(card)
					player["hand"].reverse()

				player["deck"] = list([])

		for player in self.getPlayers():
			if(len(player["hand"])):
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

	def __rules(self) -> None: # Application des règles du jeu
		for player in self.getPlayers():
			if((len(player["hand"]) + len(player["deck"])) == 52):
				self.__end		= bool(True)
				self.__winner	= dict(player)

	def start(self) -> bool: # Lancement de la partie
		self.mixCards()
		self.__distrib()

		while(not self.__end):
			self.__round += 1
			print(f"{(' ')*len(self.getPlayers())}{('-'*5)*len(self.getPlayers())} {self.content['_ROUND']}: {self.__round} {('-'*5)*len(self.getPlayers())}")
			self.__update()
			self.__displayCardOnTable()
			self.__clearTable()
			self.__rules()

			print("")
			for player in self.getPlayers():
				print(f" {player['name']}: {len(player['hand']) + len(player['deck'])}")

			print("")
			# input()

		print(f" {self.__winner['name']} {self.content['_WINNER']} !")

		return(True)