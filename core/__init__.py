#!/bin/python3
# -*- coding: utf-8 -*-

from time import sleep
from traceback import format_exc

from core.b64 import B64
from core.cards import Cards
from core.config import Config
from core.colors import Colors
from core.icons import Icons
from core.players import LoadPlayers, Players
from core.regions import Regions

from games import games

def launch(cfg: dict, reg: dict, game) -> bool: # Fonction de lancement du jeu
	game = game(reg, cfg.encoding)
	print(f"{Icons.play}{game.gameName}")

	if(not game.finished):
		print(f"{Icons.warn}{reg['GAME_NOTFINISHED']}")

	try:
		return(game.start())

	except Exception:
		print(f"{Icons.warn}{format_exc()}")

	return(False)

def splash(reg: dict, info: dict) -> bool: # Splash Screen
	for row in tuple((
		"                      {}_        ______{}".format(Colors.yellow, Colors.end),
		"                     {}| |      / ____/{}".format(Colors.yellow, Colors.end),
		"  {}____ ___ _ _ __ ___| |  ___/ /   ___ ___ _ _ _ _ __   ___   ___{}".format(Colors.yellow, Colors.end),
		" {}/ __// _ ` | `_// _ ` | / _/ |   |_  / _ ` | `_` `_ \ / _ \ | _ \_ __{}".format(Colors.yellow, Colors.end),
		"{}| (__| (_)  | | | (_)  |_\ \ \ \___/ | (_)  | | | | | |  __/ |  _/\` /\t{}{}{}".format(Colors.yellow, Colors.red, info["vers"], Colors.end),
		" {}\__/ \___,_|_|  \___,_|___/  \_____/ \___,_|_| |_| |_|\___|.|_|  / /\t{}{} {}{}".format(Colors.yellow, Colors.purple, reg["COMMON_BY"], info["author"], Colors.end),
		"                                                                 {}/_/{}\n".format(Colors.yellow, Colors.end)
	)):
		print(row)
		sleep(.1)

	return(True)

def sortGames(cfg: dict, reg: dict) -> None:
	print(f" [ {reg['COMMON_GAMES']} ]:\n --{'-'*len(reg['COMMON_GAMES'])}--")
	print(f" *  {reg['COMMON_NAME']}{' '*(21-len(reg['COMMON_NAME']))}{reg['COMMON_PLAYABLE']}{' '*(12-len(reg['COMMON_PLAYABLE']))}{reg['COMMON_PATH']}")
	for i, game in enumerate(games):
		g = game(reg, cfg.encoding)
		finished = str(f"{Colors.green}{reg['COMMON_YES']}{Colors.end}" if(g.finished) else f"{Colors.red}{reg['COMMON_NO']}{Colors.end}")
		print(f" {Colors.cyan}{i+1}{Colors.end}. {Colors.yellow}{g.gameName}{Colors.end}{' '*(21-len(g.gameName))}{finished}{' '*(21-len(finished))}{g.__file__}")

	print("")

def sortPlayers(cfg: dict, reg: dict) -> None:
	players = Players(cfg.encoding)

	print(f" [ {reg['COMMON_PLAYERS']} ]:\n --{'-'*len(reg['COMMON_PLAYERS'])}--")
	print(f" *  {reg['COMMON_NAME']}")
	for i, player in enumerate(players.getPlayerNames()):
		print(f" {Colors.cyan}{i+1}{Colors.end}. {Colors.yellow}{player}{Colors.end}")

	print("")