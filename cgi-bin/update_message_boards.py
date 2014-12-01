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
	print "User not recognized; only logged-in users can comment."
	exit(1)

def add_message(msg, email, board):
	board += msg + '\t' + email + '\t' + str(datetime.now()) + '\n'
	return board

def read_messages(board):
	s = ''
	if board is None or board == '':
		s = "No messages yet!"
	else:
		for line in board:
			line = line.split('\t')
			s += '(' + line[2].strip() + ') ' + line[1] + ':\t' + line[0] + '\n'
	return s

cgitb.enable()
form = cgi.FieldStorage()

(event, new_message, update) = (
	form['event'].value,
	form['new_message'].value,
	int(form['update'].value)
)
if not update:
	print "Content-type: text/html"
	print
	print read_messages()
	exit(0)

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
	
cur.execute("SELECT msg_brd FROM events WHERE id = ?", (event,))
board = cur.fetchone()[0]
board = add_msg(new_message, email, board)
cur.execute("UPDATE TABLE events SET msg_brd = ? WHERE id = ?", (board, event))

print "Content-type: text/html"
print
print read_messages()
