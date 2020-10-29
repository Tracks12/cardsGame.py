#!/bin/python3
# -*- coding: utf-8 -*-

# testeur auto de programme python

from platform import system
from os import system as shell
from time import sleep

while(True):
	shell("clear" if(system() == "Linux") else "cls")
	shell("python3 main.py")
	sleep(.5)
