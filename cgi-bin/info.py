#!/usr/bin/python

import cgi
import cgitb
import sqlite3

def build_html_page(content_line, cookie=None):
	s = ''
 	s += ("Content-Type: text/html\n")
 	if cookie is not None:
 		print cookie
 	s += ("\n<html>")
 	s += ("<body>")
 	s += ("<p>" + content_line + "\n")
 	s += ("</body>")
 	s += ("</html>")
 	return s

cgitb.enable()

conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
c = conn.cursor()
c.execute("SELECT * from pros")
res = c.fetchall()

#make list res into a string and print it in the html page

print res
c.close()
conn.close()