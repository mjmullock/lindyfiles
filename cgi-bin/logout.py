#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import Cookie

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
form = cgi.FieldStorage()
logout = form['logout'].value

if logout:
	c = Cookie.SimpleCookie()
	c['expires'] = 'Sun, 26 Oct 2014 00:00:01 GMT'
	page = build_html_page('Goodbye.', cookie=c)

print page
exit(0)
