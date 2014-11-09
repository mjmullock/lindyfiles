#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import Cookie
import os

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
	oldc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
	if oldc is None:
		page = build_html_page('Error finding your current cookie. :(')
	else:
		c = Cookie.SimpleCookie()
		a = oldc['sessid']
		c['sessid'] = a
		c['sessid']['expires'] = 'Sun, 26 Oct 2014 00:00:01 GMT'
		page = build_html_page('Goodbye.', cookie=c)

print page
exit(0)
