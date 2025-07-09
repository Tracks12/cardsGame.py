#!/bin/python3
# -*- coding: utf-8 -*-

try:
	# --- Importing external dependencies ---
	from os import environ, listdir, system as shell
	from platform import system
	from sys import argv, version_info

	if(version_info.major < 3): # Check if Python version is 3 or higher
		raise(RuntimeError)
	
	if(system() == "Linux"): # Dependencies for Linux
		import readline

	# Importation des dépendances internes
	from core import *
	from core.constants import CMD_CLEAR, CMD_PYTHON

except(RuntimeError):
	print("/!\\ - Program must be run with Python 3")
	exit()

except(ModuleNotFoundError) as e:
	print(f"/!\\ - ImportError: {e}")
	exit()

def arg(cfg: Config, reg: dict) -> bool: # Fonction d'entrée des arguments
	args = dict({
		"prfx": tuple[tuple[tuple[str], str]]((
			(("-s", "--show-card"), "<x>"),
			(("-S", "--show-all"), ""),
			(("-r", "--show-rand-card"), "<x>"),
			(("-R", "--show-rand-all"), ""),
			(("-g", "--game"), "<gameName>"),
			(("-p", "--players"), "\"['name', ...]\""),
			(("-l", "--list"), "players|games"),
			(("-h", "--help"), ""),
			(("-D", "--debug"), ""),
			(("-v", "--version"), "")
		)),
		"desc": tuple[str](reg["ARGS_DESC"])
	})

	if(argv[1] in args["prfx"][-3][0]): # Affiche le helper args
		print(f" {reg['ARGS_INTRO'][0]}")
		print(f" {reg['ARGS_INTRO'][1]}: python main.py <arg>\n")
		print(f" {reg['ARGS_INTRO'][2]}:")

		for i in range(0, len(args["prfx"])):
			leftSide = f"{args['prfx'][i][0][0]}, {args['prfx'][i][0][1]} {args['prfx'][i][1]}"
			print(f" {leftSide}{' '*(32-len(leftSide))}{args['desc'][i]}", end="\n\n" if(i in (3, 6, len(args['desc'])-1)) else "\n")

	elif(argv[1] in args["prfx"][-2][0]): # Mode Debugger
		environ["CG_DEBUG"] = "1" # Set DEBUG environment variable to 1

		while(True):
			shell(CMD_CLEAR)
			print(f"{Icons.info}{reg['DEBUG_STARTING']}")
			shell(f"{CMD_PYTHON} {__file__}")
			input(f"{Icons.info}{reg['DEBUG_CONTINUE']}")

	elif(argv[1] in args["prfx"][-1][0]): # Affiche la version du script
		print(f" {INFO['name']} {INFO['vers']} {reg['COMMON_BY']} {INFO['author']}\n")

	elif(argv[1] in args["prfx"][0][0]): # Affiche une carte du paquet
		packets = Cards(2)

		try:
			card = int(argv[2])-1

		except(Exception):
			print(f"{Icons.warn}{reg['ERR_CARD_NUMBER']}")
			return(False)

		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][1][0]): # Affiche tout le paquet
		packets = Cards(2)
		packets.dispAllCards()

	elif(argv[1] in args["prfx"][2][0]): # Affiche une carte du paquet mélangé
		packets = Cards(2)

		try:
			card = int(argv[2])-1

		except(Exception):
			print(f"{Icons.warn}{reg['ERR_CARD_NUMBER']}")
			return(False)

		packets.mixCards()
		packets.dispOneCard(card)

	elif(argv[1] in args["prfx"][3][0]): # Affiche tout le paquet mélangé
		packets = Cards(2)
		packets.mixCards()
		packets.dispAllCards()

	elif(argv[1] in args["prfx"][4][0]): # Lance un mode de jeu choisis en arguments
		try:
			gameName = str(argv[2])

		except(Exception):
			print(f"{Icons.warn}{reg['ERR_GAME_NAME']}")
			return(False)

		gameList = list[str]([])
		for game in GAMES:
			gameList.append(game(reg, cfg.encoding).gameName)

		for id, name in enumerate(gameList):
			if(gameName == name):
				launch(cfg, reg, GAMES[id])

	elif(argv[1] in args["prfx"][5][0]): # Gestion des joueurs
		try:
			playersList = list(eval(argv[2]))

		except(Exception):
			print(f"{Icons.warn}{reg['ERR_PLAYER_LIST']}")
			return(False)

		players	= LoadPlayers(cfg.encoding)
		players.insert(playersList)

	elif(argv[1] in args["prfx"][6][0]): # Affiche toute la configuration
		try:
			if(argv[2] == "games"):
				sortGames(cfg, reg)

			elif(argv[2] == "players"):
				sortPlayers(cfg, reg)

			else:
				print(f"{Icons.warn}{reg['ERR_LIST']}")
				return(False)

		except(Exception):
			sortGames(cfg, reg)
			sortPlayers(cfg, reg)

	else:
		print(f'{Icons.warn}{reg["ERR_ARGS"]} "{argv[1]}"')

	return(True)

def playerManager(cfg: Config, reg: dict) -> bool:
	menu = tuple((
		"",
		reg['MENU_PLAYER_CONTENT_LIST'],
		reg['MENU_PLAYER_CONTENT_ADD'],
		reg['MENU_PLAYER_CONTENT_REMOVE']
	))

	for key, row in enumerate(menu):
		print(f" {f'{Colors.cyan}{key}.{Colors.end}' if(key > 0) else ''} {row}", end="\n\n" if(key == len(menu)-1) else "\n")

	print(f" {Colors.red}0.{Colors.end} {reg['COMMON_BACK']}", end="\n\n")

	while(True):
		while(True):
			try:
				choice = int(input(f"({Colors.green}{INFO['name']}{Colors.end})[{Colors.yellow}{reg['MENU_PLAYER_LABEL']}{Colors.end}]> {Colors.cyan}"))
				print(end=Colors.end)
				break

			except(Exception):
				print(f"{Icons.warn}{reg['ERR_MENU_CHOICE']}")

		if(choice == 0):
			break

		elif(choice == 1):
			print("")
			sortPlayers(cfg, reg)

		elif(choice == 2):
			newPlayer = str(input(f"{reg['MENU_PLAYER_INPUT_NAME']}: {Colors.cyan}"))

			players = Players(cfg.encoding)
			newPlayerList = list(players.getPlayerNames())
			newPlayerList.append(newPlayer)

			loadedPlayers	= LoadPlayers(cfg.encoding)
			loadedPlayers.insert(newPlayerList)

			print(f"{Icons.info}{reg['COMMON_PLAYER']} {newPlayer} {reg['MENU_PLAYER_RESULT_ADDED']}")

		elif(choice == 3):
			print("")
			sortPlayers(cfg, reg)

			try:
				playerId = int(input(f"{reg['MENU_PLAYER_INPUT_NUMBER']}: {Colors.cyan}"))

				players = Players(cfg.encoding)
				newPlayerList = list(players.getPlayerNames())
				playerName = str(newPlayerList.pop(playerId-1))

				loadedPlayers	= LoadPlayers(cfg.encoding)
				loadedPlayers.insert(newPlayerList)

				print(f"{Icons.info}{reg['COMMON_PLAYER']} {playerName} {reg['MENU_PLAYER_RESULT_DELETED']}")

			except(Exception):
				print(f"{Icons.warn}{reg['ERR_PLAYER_EXIST']}")

		else:
			print(f"{Icons.warn}{reg['ERR_MENU_CHOICE']}")

	return(True)

def config(cfg: Config, reg: dict) -> bool: # Fonction de configuration du programme
	def confirm(setter: bool) -> bool:
		if(setter):
			print(f"{Icons.info}{reg['MENU_CONFIG_SUCCESS']}")
			return(True)

		print(f"{Icons.warn}{reg['MENU_CONFIG_FAIL']}")
		return(False)

	menu = tuple((
		"",
		f"{'Colors':<{24}}[ {cfg.colors} ]",
		f"{reg['MENU_CONFIG_CONTENT_ENCODING']:<{24}}[ {cfg.encoding} ]",
		f"{reg['MENU_CONFIG_CONTENT_LANGUAGE']:<{24}}[ {cfg.language} ]",
		f"{reg['MENU_CONFIG_CONTENT_SPLASH']:<{24}}[ {cfg.splash} ]"
	))

	for key, row in enumerate(menu):
		print(f" {f'{Colors.cyan}{key}.{Colors.end}' if(key > 0) else ''} {row}", end="\n\n" if(key == len(menu)-1) else "\n")

	print(f" {Colors.red}0.{Colors.end} {reg['COMMON_BACK']}", end="\n\n")

	while(True):
		while(True):
			try:
				choice = int(input(f"({Colors.green}{INFO['name']}{Colors.end})[{Colors.yellow}{reg['MENU_CONFIG_LABEL']}{Colors.end}]> {Colors.cyan}"))
				print(end=Colors.end)
				break

			except(Exception):
				print(f"{Icons.warn}{reg['ERR_MENU_CHOICE']}")

		if(choice == 0):
			print(f"{Icons.info}{reg['MENU_CONFIG_RESTART']}")
			break

		elif(choice == 1):
			prompt = str(f"[{Colors.green}true{Colors.end}|{Colors.red}false{Colors.end}]")
			colors = str(input(f"Colors {prompt}: {Colors.cyan}"))
			print(end=Colors.end)

			confirm(cfg.setColors(colors))

		elif(choice == 2):
			codings = tuple(("ascii", "utf-8", "utf-16", "utf-32"))
			prompt	= str("[")

			for k, v in enumerate(codings):
				prompt += str(f"{Colors.cyan}{v}{Colors.end}{'|' if(k < len(codings)-1) else ']'}")

			coding = str(input(f"{reg['MENU_CONFIG_CONTENT_ENCODING']} {prompt}: {Colors.cyan}"))
			print(end=Colors.end)

			confirm(cfg.setEncode(coding))

		elif(choice == 3):
			langs	= list(listdir("core/regions"))
			for k, v in enumerate(langs):
				langs[k] = str(v.split(".")[0])

			prompt	= str("[")
			for k, v in enumerate(langs):
				prompt += str(f"{Colors.cyan}{v}{Colors.end}{'|' if(k < len(langs)-1) else ']'}")

			lang = str(input(f"{reg['MENU_CONFIG_CONTENT_LANGUAGE']} {prompt}: {Colors.cyan}"))
			print(end=Colors.end)

			confirm(cfg.setLanguage(lang))

		elif(choice == 4):
			prompt = str(f"[{Colors.green}true{Colors.end}|{Colors.red}false{Colors.end}]")
			colors = str(input(f"{reg['MENU_CONFIG_CONTENT_SPLASH']} {prompt}: {Colors.cyan}"))
			print(end=Colors.end)

			confirm(cfg.setSplash(colors))

		else:
			print(f"{Icons.warn}{reg['ERR_MENU_CHOICE']}")

	return(True)

def main(cfg: Config, reg: dict) -> bool: # Fonction principale de l'execution du programme
	if(cfg.splash):
		splash(reg)

	menu = list([ f"{reg['MENU_TEXT']}:\n" ])
	for game in GAMES:
		game = game(reg, cfg.encoding)
		playable = str(f"{Colors.green+reg['COMMON_PLAYABLE'] if(game.finished) else Colors.red+reg['COMMON_UNPLAYABLE']}{Colors.end}")
		menu.append(str(f"{game.gameName}{' '*(24-len(game.gameName))}[ {playable} ]"))

	for key, row in enumerate(menu):
		print(f" {'' if(key == 0) else f'{Colors.cyan}{key}.{Colors.end} '}{row}", end="\n\n" if(key == len(menu)-1) else "\n")

	print( f" {Colors.yellow}{len(menu)}.{Colors.end} {reg['MENU_CHOICE_PLAYER']}")
	print( f" {Colors.yellow}{len(menu)+1}.{Colors.end} {reg['MENU_CHOICE_SETTINGS']}")
	print( f" {Colors.red}0.{Colors.end} {reg['MENU_CHOICE_QUIT']}", end="\n\n")

	while(True):
		while(True):
			try:
				choice = int(input(f"({Colors.green}{INFO['name']}{Colors.end})> {Colors.cyan}"))
				print(end=Colors.end)
				break

			except(Exception):
				print(f"{Icons.warn}{reg['ERR_MENU_CHOICE']}")

		for i, game in enumerate(GAMES):
			if(choice == i+1):
				launch(cfg, reg, game)

		if(choice == 0):
			break

		elif(choice == len(menu)):
			playerManager(cfg, reg)

		elif(choice == len(menu)+1):
			config(cfg, reg)

	return(True)

if(__name__ == "__main__"):
	cfg = Config() # Chargement du fichier de configuration
	reg = Regions(cfg.language, cfg.encoding).content # Chargement de la langue

	if(len(argv) > 1):
		arg(cfg, reg)

	else:
		main(cfg, reg)
