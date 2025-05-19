#!/bin/python3
# -*- coding: utf-8 -*-

from core import Colors
from core.cards import Cards
from core.players import Players

class Solitary(Cards, Players): # Le solitaire
	def __init__(self, lang: dict, encode: str):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.__file__ = __file__
		self.content	= dict(lang["GAME_SOLITARY"])
		self.gameName	= str(self.content["_NAME"])
		self.finished	= bool(False)
		self.__end		= bool(False)
		self.__table	= list([])

	def __update(self) -> None:
		self.__end = bool(True)

	def start(self) -> bool:
		while(not self.__end):
			self.__update()

		return(True)