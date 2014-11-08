#!/usr/bin/python

import cgi
import cgitb
import os

cgitb.enable()
form = cgi.FieldStorage()
new_message = form['stuff'].value

with open("message_board.txt", "a") as f:
	f.write(new_message)
	f.write("\n")
	f.close()

s = ''
with open("message_board.txt", "r+") as f:
	for line in f:
		s += line + '\n'

print "Content-type: text/html"
print
print s
