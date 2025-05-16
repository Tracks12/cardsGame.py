#!/bin/python3
# -*- coding: utf-8 -*-

from core import Colors
from core.cards import Cards
from core.players import Players

class Chickenshit(Cards, Players): # Le pouilleux ou mistigri
	def __init__(self, lang, encode):
		Cards.__init__(self, 1)
		Players.__init__(self, str(encode))

		self.__file__ = __file__
		self.content	= dict(lang["GAME_CHICKENSHIT"])
		self.gameName	= str(self.content["_NAME"])
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