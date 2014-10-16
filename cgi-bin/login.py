#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import os
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

cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string:
	c = Cookie.SimpleCookie(cookie_string)
	print build_html_page("I have your cookie!")
	exit(0)
else:
	c = Cookie.SimpleCookie()
	c['name'] = 'test_cookie'
	print build_html_page("Building cookie...", cookie=c)
	exit(0)
    

form = cgi.FieldStorage()
name = form["name"].value
password = form['password'].value
signup_type = form['signup_type'].value
if signup_type not in ['register', 'login']:
	print build_html_page("Signup type incorrectly specified.")
	exit(0)


conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
c = conn.cursor()
c.execute("select * from users where fname=?;", (name,))
res = c.fetchall()

if not len(res):
	if signup_type == 'register':
		c.execute("insert into users (fname, password) values(?,?);", (name,password))
		conn.commit()
		page = build_html_page("Welcome, " + name)
	else:
		page = build_html_page("Sorry, user '" + name + "' not found.")
else:
	if signup_type == 'register':
		page = build_html_page("Sorry, that name is already in use.")
	elif len(res) != 1:
		page = build_html_page("Database consistency error, multiple results with the same name")
	else:
		if password == res[0][1]:
			page = build_html_page("Welcome back, " + name + ".")
		else:
			page = build_html_page("Login error: incorrect password entered.")

print page
exit(0)
