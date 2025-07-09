#!/bin/python3
# -*- coding: utf-8 -*-

from importlib import import_module
from inspect import getmembers, isclass
from pkgutil import iter_modules

from core import Game
from core.constants import DEBUG

if(DEBUG):
	print("[games] Importing games...")

GAMES: list[Game] = []

for _, module, _ in iter_modules(__path__):
	if(module == "__init__"):
		continue

	game = str(f"{__name__}.{module}")

	try:
		module = import_module(game)

		for _, obj in getmembers(module, isclass):
			if(issubclass(obj, Game) and obj is not Game):
				GAMES.append(obj)

				if(DEBUG):
					print(f"[games] Registered game: {obj.__name__} ({game})")

	except(Exception) as e:
		if(DEBUG):
			print(f"[games] Failed to import game {game}: {e}")

if(DEBUG):
	print(f"[games] Total games imported: {len(GAMES)}")