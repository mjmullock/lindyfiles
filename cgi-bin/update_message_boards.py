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
	if board is None:
		board = ''
	board += msg + '\t' + email + '\t' + str(datetime.now()) + '\n'
	return board

def read_messages(board):
	s = ''
	if board is None or board == '':
		s = "No messages yet!"
	else:
		lines = board.split('\n')
		for line in lines:
			if line is None or line == '':
				continue
			try:
				line = line.split('\t')
				s += '(' + line[2].strip() + ') ' + line[1] + ':\t' + line[0] + '\n'
			except IndexError:
				print "Content-type: text/html"
				print
				print "Error" + str(line)
				exit(1)
	return s

cgitb.enable()
form = cgi.FieldStorage()

(event, new_message, update) = (
	form['event'].value,
	form['new_message'].value,
	int(form['update'].value)
)
conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
cur = conn.cursor()
cur.execute("SELECT msg_brd FROM events WHERE id = ?", (event,))
board = cur.fetchone()[0]

if not update:
	print "Content-type: text/html"
	print
	print read_messages(board)
	exit(0)

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

board = add_message(new_message, email, board)
cur.execute("UPDATE events SET msg_brd = ? WHERE id = ?", (board, event))
conn.commit()

print "Content-type: text/html"
print
print read_messages(board)
