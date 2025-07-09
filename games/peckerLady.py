#!/bin/python3
# -*- coding: utf-8 -*-

from core.cards import Card, Cards
from core.game import Game
from core.players import Player, Players

class PeckerLady(Cards, Game, Players): # La dame de pic
	def __init__(self, lang: dict, encode: str):
		Cards.__init__(self)
		Players.__init__(self, str(encode))

		Game.__init__(self, dict({
			"__file__"	: str(__file__),
			"content"	: dict(lang["GAME_PECKERLADY"]),
			"finished"	: bool(False)
		}))

		self.__end		: bool						= bool(False)
		self.__round	: int						= int(0)
		self.__table	: list[tuple[str, Card]]	= list[tuple[str, Card]]([]) # Plateau
		self.__winner	: Player					= None

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