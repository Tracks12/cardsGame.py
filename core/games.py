#!/bin/python3
# -*- coding: utf-8 -*-

from core.cards import Cards

class ClosedBattle(Cards):
	game = "la bataille fermée"

	def getCards(self):
		self.getAllCards()

class Solitary(Cards):
	game = "le solitaire"

class PeckerLady(Cards):
	game = "la dame de pic"

class Chickenshit(Cards):
	game = "le pouilleux"

class Liar(Cards):
	game = "le menteur"
