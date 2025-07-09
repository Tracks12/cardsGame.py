#!/bin/python3
# -*- coding: utf-8 -*-

from os import getenv
from platform import system

__isLinux		= system() == "Linux"

CMD_CLEAR		= "clear" if(__isLinux) else "cls"
CMD_PYTHON		= "python3" if(__isLinux) else "python"
DEBUG			= bool(getenv("CG_DEBUG", "0") == "1")
ENABLE_COLOR	= bool(system() == "Linux")
