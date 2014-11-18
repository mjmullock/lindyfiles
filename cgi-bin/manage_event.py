#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import Cookie
import os

def main():
	attendees_implemented = 0
	
	cgitb.enable()
	cookie = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE"))
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	cur = conn.cursor()
	form = cgi.FieldStorage()
	try:
		eventID = form['eventID'].value
	except KeyError:
		eventID = 2
	
	if attendees_implemented:
		cur.execute("select attendees from events where id=?", (eventID,))
		res = str(cur.fetchone())
	else:
		res = ""
		
	sessid = cookie["sessid"].value
	cur.execute("select email from users where sessid=?", (sessid,))
	email = cur.fetchone()
	res += str(email)
	if attendees_implemented:
		cur.execute("update events set attendees=? where id=?", (res, eventID))
	
	cur.close()
	conn.close()
	print "Content-type: text\html"
	print
	print res
	
if __name__ == "__main__":
	main()
