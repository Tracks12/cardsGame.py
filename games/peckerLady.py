#!/bin/python3
# -*- coding: utf-8 -*-

from core import Colors
from core.cards import Cards
from core.players import Players

class PeckerLady(Cards, Players): # La dame de pic
	def __init__(self, lang, encode):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.__file__ = __file__
		self.content	= dict(lang["GAME_PECKERLADY"])
		self.gameName	= str(self.content["_NAME"])
		self.finished	= bool(False)
		self.__end		= bool(False)
		self.__round	= int(0)
		self.__table	= list([])
		self.__winner	= None

	def __update(self) -> None:
		self.__end = bool(True)

	def __rules(self) -> None:
		for player in self.players:
			if(player["score"] >= 100):
				self.end = bool(True)

	def start(self) -> bool:
		while(not self.__end):
			self.__update()

		return(True)