#!/usr/bin/python

import cgi
import cgitb
import os
import sqlite3
import Cookie
from datetime import datetime

cgitb.enable()
form = cgi.FieldStorage()
new_message = form['stuff'].value
conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
cur = conn.cursor()

def do_err():
	print "Content-type: text/html"
	print
	print "User not recognized. Only logged-in users can view the message board."
	exit(1)

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

with open("message_board.txt", "a") as f:
	msg = str( (new_message, email, str(datetime.now())) )
	f.write(msg)
	f.write("\n")
	f.close()

s = ''
with open("message_board.txt", "r+") as f:
	for line in f:
		s += line + '\n'

print "Content-type: text/html"
print
print s
