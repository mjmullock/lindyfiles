#!/usr/bin/python

import cgi
import cgitb
import os

def make_page():
	s = "Content-Type: text/html\n\n"
	s += '<html>\n'
	s += '<body>\n'
	
	with open("message_board.txt", "r+") as f:
		for line in f:
			s += line + '\n'

	s += '</body>\n'
	s += '</html>'
	print s

cgitb.enable()
make_page()
