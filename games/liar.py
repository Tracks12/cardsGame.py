#!/bin/python3
# -*- coding: utf-8 -*-

from core import Colors
from core.cards import Cards
from core.players import Players

class Liar(Cards, Players): # Le menteur
	def __init__(self, lang: dict, encode: str):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		self.__file__	: str 	= str(__file__)
		self.content	: dict	= dict(lang["GAME_LIAR"])
		self.gameName	: str	= str(self.content["_NAME"])
		self.finished	: bool	= bool(False)
		self.__end		: bool	= bool(False)
		self.__round	: int	= int(0)
		self.__table	: list	= list([])
		self.__winner			= None

	def __update(self) -> None:
		self.__end = bool(True)

	def start(self) -> bool:
		while(not self.__end):
			self.__update()

		return(True)