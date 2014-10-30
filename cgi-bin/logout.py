#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import os
import Cookie
from datetime import datetime

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
	c = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
	c['expires'] = datetime.now()
	page = build_html_page('Goodbye.', cookie=c)

print page
exit(0)
