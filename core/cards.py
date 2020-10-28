#!/bin/python3
# -*- coding: utf-8 -*-

from core.colors import Colors

class Cards: # Objet de jeu de cartes
	def __init__(self): # Construction du jeu de 52 cartes
		self.packets = []
		self.__numbers = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "Q", "R")
		self.__shapes  = ("♥", "♦", "♠", "♣")

		for s in self.__shapes:
			for n in self.__numbers:
				self.packets.append([n, s])

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

	def getAllCards(self): # Affiche toutes les cartes en ascii
		for card in self.packets:
			self.__dispCard(card)

		return self.packets

	def getOneCard(self, key):
		card = self.packets[key]
		self.__dispCard(card)

		return card
