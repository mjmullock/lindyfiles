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
	cur = conn.cursor()
	ck_string = os.environ.get('HTTP_COOKIE')
	if not ck_string:
		do_err("User not logged in.")

	form = cgi.FieldStorage()
	field_name = form['fieldName'].value
	new_val = form['newValue'].value

	ck = Cookie.SimpleCookie(ck_string)
	sessid = ck['sessid'].value

	try:
		cur.execute("UPDATE users SET " + str(field_name) + "=? WHERE sessid=?", (new_val, sessid))
		conn.commit()
	except Exception as e:
		err_string = str(e) + '\t' + field_name + str(new_val) + sessid + "Could not make modification: user not recognized."
		do_err(err_string)

	print "Content-type: text/html"
	print
	print new_val

if __name__ == '__main__':
	main()
