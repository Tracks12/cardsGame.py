#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création de packet de carte

from random import shuffle

from core.colors import Colors

class Cards: # Objet de jeu de cartes
	def __init__(self, joker = int(0)): # Construction du jeu de 52 cartes avec/sans les jokers
		self._packet	= list([])
		self.__numbers	= tuple(("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "Q", "K"))
		self.__shapes	= tuple(("♥", "♦", "♠", "♣"))

		self.__buildPacket(joker)

	def __buildPacket(self, joker) -> list: # Construction du packet de cartes
		for s in self.__shapes: # Ajout des 52 cartes
			for n in self.__numbers:
				self._packet.append(tuple((n, s)))

		for j in range(0, joker): # Ajout des cartes jokers
			self._packet.append(tuple(("J", "★")))

		return(self._packet)

	def __dispCard(self, card) -> list: # Affichage d'une carte
		color = str(Colors.red if(card[1] in ("♥", "♦")) else Colors.cyan)

		displayer = tuple((
			",-----,",
			f"|{color}{card[0]}{' ' if(len(card[0]) < 2) else ''}{Colors.end}   |",
			f"|  {color}{card[1]}{Colors.end}  |",
			f"|   {color}{' ' if(len(card[0]) < 2) else ''}{card[0]}{Colors.end}|",
			"`-----`"
		))

		for line in displayer:
			print(line)

		return(card)

	def dispAllCards(self) -> list: # Affiche toutes les cartes en ascii
		cards = list(self.getAllCards())

		for card in cards:
			self.__dispCard(card)

		return(cards)

	def dispOneCard(self, key) -> list: # Affiche une carte en ascii
		card = list(self.getOneCard(key))
		self.__dispCard(card)

		return(card)

	def mixCards(self) -> list: # mélange les cartes du packets
		shuffle(self._packet)

		return(self._packet)

	def getAllCards(self) -> list: # Sort toutes les cartes
		return(self._packet)

	def getOneCard(self, key) -> tuple: # Sort une carte
		return(self._packet[key])
