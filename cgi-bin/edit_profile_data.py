#!/usr/bin/python

import cgi
import cgitb
import os
import sqlite3
import Cookie

def do_err(s):
	print "Content-type: text/html"
	print
	print s
	exit(1)

def main():
	
	cgitb.enable()
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	c = conn.cursor()
	ck_string = os.environ.get('HTTP_COOKIE')
	if not ck_string:
		do_err("User not logged in.")

	form = cgi.FieldStorage()
	field_name = form['fieldName'].value
	new_val = form['newVal'].value

	ck = Cookie.SimpleCookie(cookie_string)
	sessid = ck['sessid'].value

	try:
		c.execute("UPDATE users SET ? = ? WHERE sessid = ?", (field_name, new_val, sessid))
		conn.commit()
	except:
		do_err("Could not make modification: user not recognized.")

	print "Content-type: text/html"
	print
	print new_val

if __name__ == '__main__':
	main()
