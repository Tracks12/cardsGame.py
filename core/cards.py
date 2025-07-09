#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création de packet de carte

from random import shuffle

from core.colors import Colors

class Card:
	def __init__(self, props: tuple[str]):
		self.number	: str	= str(props[0])
		self.shape	: str	= str(props[1])

class Cards: # Objet de jeu de cartes
	def __init__(self, joker: int = 0): # Construction du jeu de 52 cartes avec/sans les jokers
		self._packet	: list[Card]	= list([])
		self.__numbers	: tuple[str]	= tuple[str](("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "Q", "K"))
		self.__shapes	: tuple[str]	= tuple[str](("♥", "♦", "♠", "♣"))

		self.__buildPacket(joker)

	def __buildPacket(self, joker: int) -> list[Card]: # Construction du packet de cartes
		for s in self.__shapes: # Ajout des 52 cartes
			for n in self.__numbers:
				self._packet.append(Card((n, s)))

		for j in range(0, joker): # Ajout des cartes jokers
			self._packet.append(Card(("J", "★")))

		return(self._packet)

	def __dispCards(self, cards: list[Card]) -> list[Card]: # Affichage d'une carte
		displayer = list[str](["", "", "", "", ""])

		for card in cards:
			color = str(Colors.red if(card.shape in ("♥", "♦")) else Colors.cyan)

			displayer[0] += " ,-----,"
			displayer[1] += f" |{color}{card.number}{' ' if(len(card.number) < 2) else ''}{Colors.end}   |"
			displayer[2] += f" |  {color}{card.shape}{Colors.end}  |"
			displayer[3] += f" |   {color}{' ' if(len(card.number) < 2) else ''}{card.number}{Colors.end}|"
			displayer[4] += " `-----`"

		for line in displayer:
			print(line)

		return(cards)

	def dispAllCards(self, div: int = 6) -> list[Card]: # Affiche toutes les cartes en ascii
		cards = self.getAllCards()

		for i in range(0, int(len(cards) / div)):
			self.__dispCards(cards[i*div:(i*div)+div])

		return(cards)

	def dispOneCard(self, key: int) -> Card: # Affiche une carte en ascii
		card = self.getOneCard(key)
		self.__dispCards([ card ])

		return(card)

	def mixCards(self) -> list[Card]: # mélange les cartes du packets
		shuffle(self._packet)

		return(self._packet)

	def getAllCards(self) -> list[Card]: # Sort toutes les cartes
		return(self._packet)

	def getOneCard(self, key: int) -> Card: # Sort une carte
		return(self._packet[key])
