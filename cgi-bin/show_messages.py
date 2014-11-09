#!/usr/bin/python

import cgi
import cgitb
import os
import sqlite3
import Cookie
from datetime import datetime


def do_err():
	print "Content-type: text/html"
	print
	print "User not recognized."
	print "Only logged-in users can view the message board."
	exit(1)

def clear():
	open("message_board.txt", "w").close()

def add_msg(new_message, email):
	with open("message_board.txt", "a") as f:
		msg = new_message + '\t' + email + '\t' + str(datetime.now())
		f.write(msg)
		f.write("\n")
		f.close()

def read_messages():
	s = ''
	if os.path.getsize("message_board.txt") <= 0:
		s = "No messages yet!"
	else:
		with open("message_board.txt", "r+") as f:
			for line in f:
				line = line.split('\t')
				s += line[0] + '\t' + line[1] + ', ' + line[2] + '\n'
	return s

def get_inputs():
	initial = int(form['initial'].value)
	if initial:
		return (initial, 0, 0)
	clear_messages = int(form['clear'].value)
	if clear:
		return (initial, clear, 0)
	return (initial, clear, form['stuff'].value)

cgitb.enable()
form = cgi.FieldStorage()

(initial, clear_messages, new_message) = get_inputs()
conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
cur = conn.cursor()

cookie_string = os.environ.get('HTTP_COOKIE')
if not cookie_string:
	do_err()

try:
	ck = Cookie.SimpleCookie(cookie_string)
	sessid = ck['sessid'].value
	cur.execute("SELECT email FROM users WHERE sessid = ?", (sessid,))
	results = cur.fetchone()
	email = results[0]
except:
	do_err()

if clear_messages:
	clear()
elif not initial:
	add_msg(new_message, email)

print "Content-type: text/html"
print
print read_messages()
