#!/bin/python3
# -*- coding: utf-8 -*-

from core import Game

from games.chickenshit import Chickenshit
from games.closedBattle import ClosedBattle
from games.heightAmericans import HeightAmerican
from games.liar import Liar
from games.peckerLady import PeckerLady
from games.solitary import Solitary

GAMES = list[Game]([ # Registre des jeux
	ClosedBattle,
	Chickenshit,
  HeightAmerican,
	Liar,
	PeckerLady,
	Solitary,
])