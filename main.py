#!/bin/python3
# -*- coding: utf-8 -*-

from sys import argv

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

		print(",-----,")
		print("|{}   |".format(card[0]))
		print("|  {}  |".format(card[1]))
		print("|   {}|".format(card[0]))
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

def arg():
	return(True)

def main():
	packets = Cards()
	packets.getOneCard(0)

	return(True)

if __name__ == "__main__":
	if(len(argv) > 1):
		arg()

	else:
		main()
