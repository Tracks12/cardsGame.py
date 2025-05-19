#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création de packet de carte

from random import shuffle

from core.colors import Colors

class Cards: # Objet de jeu de cartes
	def __init__(self, joker: int = 0): # Construction du jeu de 52 cartes avec/sans les jokers
		self._packet	= list([])
		self.__numbers	= tuple(("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "Q", "K"))
		self.__shapes	= tuple(("♥", "♦", "♠", "♣"))

		self.__buildPacket(joker)

	def __buildPacket(self, joker: int) -> list: # Construction du packet de cartes
		for s in self.__shapes: # Ajout des 52 cartes
			for n in self.__numbers:
				self._packet.append(tuple((n, s)))

		for j in range(0, joker): # Ajout des cartes jokers
			self._packet.append(tuple(("J", "★")))

		return(self._packet)

	def __dispCards(self, cards: list) -> list: # Affichage d'une carte
		displayer = list(["", "", "", "", ""])

		for card in cards:
			color = str(Colors.red if(card[1] in ("♥", "♦")) else Colors.cyan)

			displayer[0] += " ,-----,"
			displayer[1] += f" |{color}{card[0]}{' ' if(len(card[0]) < 2) else ''}{Colors.end}   |"
			displayer[2] += f" |  {color}{card[1]}{Colors.end}  |"
			displayer[3] += f" |   {color}{' ' if(len(card[0]) < 2) else ''}{card[0]}{Colors.end}|"
			displayer[4] += " `-----`"

		for line in displayer:
			print(line)

		return(cards)

	def dispAllCards(self, div: int = 6) -> list: # Affiche toutes les cartes en ascii
		cards = list(self.getAllCards())

		for i in range(0, int(len(cards) / div)):
			self.__dispCards(cards[i*div:(i*div)+div])

		return(cards)

	def dispOneCard(self, key: int) -> list: # Affiche une carte en ascii
		card = list(self.getOneCard(key))
		self.__dispCards([ card ])

		return(card)

	def mixCards(self) -> list: # mélange les cartes du packets
		shuffle(self._packet)

		return(self._packet)

	def getAllCards(self) -> list: # Sort toutes les cartes
		return(self._packet)

	def getOneCard(self, key: int) -> tuple: # Sort une carte
		return(self._packet[key])
