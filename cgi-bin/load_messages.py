#!/usr/bin/python

import cgi
import cgitb
import os

cgitb.enable()

with open("message_board.txt", "r+") as f:
	for line in f:
		s += line + '\n'
