#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création de packet de carte

from random import shuffle
from core.colors import Colors

class Cards: # Objet de jeu de cartes
	def __init__(self): # Construction du jeu de 52 cartes
		self._packets = []
		self.__numbers = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "Q", "R")
		self.__shapes  = ("♥", "♦", "♠", "♣")

		for s in self.__shapes:
			for n in self.__numbers:
				self._packets.append([n, s])

	def __dispCard(self, card): # Affichage d'une carte
		if(len(card[0]) < 2):
			card[0] += " "

		color = Colors.red if(card[1] in ("♥", "♦")) else Colors.cyan

		print(",-----,")
		print("|{}{}{}   |".format(color, card[0], Colors.end))
		print("|  {}{}{}  |".format(color, card[1], Colors.end))
		print("|   {}{}{}|".format(color, card[0], Colors.end))
		print("`-----`")

		return card

	def dispAllCards(self): # Affiche toutes les cartes en ascii
		cards = self.getAllCards()

		for card in cards:
			self.__dispCard(card)

		return cards

	def dispOneCard(self, key): # Affiche une carte en ascii
		card = self.getOneCard(key)
		self.__dispCard(card)

		return card

	def mixCards(self): # mélange les cartes du packets
		shuffle(self._packets)

		return True

	def getAllCards(self): # Sort toutes les cartes
		return self._packets

	def getOneCard(self, key): # Sort une carte
		return self._packets[key]
