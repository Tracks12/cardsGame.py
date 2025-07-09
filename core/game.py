#!/bin/python3
# -*- coding: utf-8 -*-

# Module de création d'objets jeux

class Game:
	def __init__(self, props: dict):
		self.__file__	: str	= str(props["__file__"])
		self.content	: dict	= dict(props["content"])
		self.gameName	: str	= str(self.content["_NAME"])
		self.finished	: bool	= bool(props["finished"])

	def start(self) -> bool:
		return(True)