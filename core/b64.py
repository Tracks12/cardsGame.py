#!/bin/python3
# -*- coding: utf-8 -*-

from base64 import b64decode, b64encode

class B64: # Encode/Decode ascii string
	def encode(str = str("")) -> str:
		return(b64encode(str.encode("ascii")).decode("ascii"))

	def decode(str = str("")) -> str:
		return(b64decode(str).decode("ascii"))