#!/bin/python3
# -*- coding: utf-8 -*-

from games.chickenshit import Chickenshit
from games.closedBattle import ClosedBattle
from games.liar import Liar
from games.peckerLady import PeckerLady
from games.solitary import Solitary

games = list([ # Registre des jeux
  ClosedBattle,
  Solitary,
  PeckerLady,
  Chickenshit,
  Liar
])