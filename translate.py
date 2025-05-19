#!/bin/python3
# -*- coding: utf-8 -*-

from csv import DictReader
from json import dumps
from os import path
from sys import argv

def arg() -> bool:
  return(True)

def main() -> bool:
  dir_path = str(path.dirname(path.realpath(__file__)))
  datas = list[str]([])
  regions = dict({})

  with open(f"{dir_path}/translations.csv", 'r', newline='') as file:
    print("[i] - Reading CSV file and load translation ...")
    lines = DictReader(file, delimiter=',')

    for line in lines:
      datas.append(line)

  print("[i] - Wrapping data in new format ...")
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

  print("[i] - Writing new regions json files ...")

  for key in regions:
    with open(f"{dir_path}/core/regions/{key}.json", 'w') as regionFile:
      string = str(dumps(regions[key], indent=2, sort_keys=True))
      regionFile.write(string)

  print("[i] - Translations created with success !")

  return(True)

if(__name__ == "__main__"):
	if(len(argv) > 1):
		arg()

	else:
		main()