#!/bin/python3
# -*- coding: utf-8 -*-

# Module des types de jeux

from core.cards import Cards

class ClosedBattle(Cards): # La bataille fermée
	game = "la bataille fermée"

class Solitary(Cards): # Le solitaire
	game = "le solitaire"

	def getCards(self):
		self.getAllCards()

class PeckerLady(Cards): # La dame de pic
	game = "la dame de pic"

class Chickenshit(Cards): # Le pouilleux ou mistigri
	game = "le pouilleux"

class Liar(Cards): # Le menteur
	game = "le menteur"
