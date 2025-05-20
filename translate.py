#!/bin/python3
# -*- coding: utf-8 -*-

from csv import DictReader
from json import dumps
from os import path
from sys import argv, version_info
from traceback import format_exc

if(version_info.major < 3): # Vérification de l'éxecution du script avec Python3
	print("/!\\ - Program must be run with Python 3")
	exit()

from core import Icons

def translates() -> bool:
	dir_path = str(path.dirname(path.realpath(__file__)))
	datas = list[str]([])
	regions = dict({})

	with open(f"{dir_path}/translations.csv", 'r', newline='') as file:
		print(f"{Icons.play}Reading CSV file and load translation ...")
		lines = DictReader(file, delimiter=',')

		for line in lines:
			datas.append(line)

	print(f"{Icons.play}Wrapping data in new format ...")
	for field in lines.fieldnames:
		if(field != 'label'):
			regions[field] = dict({})

			for data in datas:
				if(("_GAME" in data["label"]) and (data["label"].split('_')[0] == "")):
					labelSplitted = list[str](data["label"].split("_"))
					newGameLabel = str(f"{labelSplitted[1]}_{labelSplitted[2]}")
					newLabel = str(data["label"].split(f"_{newGameLabel}")[1])

					if(not newGameLabel in regions[field]):
						regions[field].update({ newGameLabel: dict({}) })

					regions[field][newGameLabel].update({ newLabel: data[field] })

				elif(("ARGS_DESC" in data["label"]) or ("ARGS_INTRO" in data["label"])):
					labelSplitted = list[str](data["label"].split("_"))
					newArgsLabel = str(f"{labelSplitted[0]}_{labelSplitted[1]}")

					if(not newArgsLabel in regions[field]):
						regions[field].update({ newArgsLabel: list([]) })

					regions[field][newArgsLabel].append(data[field])

				else:
					regions[field].update({ data["label"]: data[field] })

	print(f"{Icons.play}Writing new regions json files ...")

	for key in regions:
		with open(f"{dir_path}/core/regions/{key}.json", 'w') as regionFile:
			string = str(dumps(regions[key], indent=2, sort_keys=True))
			regionFile.write(string)

	print(f"{Icons.info}Translations created with success !")

	return(True)

def arg() -> bool:
	return(True)

def main() -> bool:
	try:
		return(translates())

	except Exception:
		print(f"{Icons.warn}{format_exc()}")
		return(False)

if(__name__ == "__main__"):
	if(len(argv) > 1):
		arg()

	else:
		main()