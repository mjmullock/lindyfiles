#!/usr/bin/python

import cgi
import cgitb
import sqlite3

def build_html_page(content_line):
	s = ''
	s += ("Content-Type: text/html\n\n")
	s += ("<html>")
	s += ("<body>")
	s += ("<p>" + content_line + "\n")
	s += ("</body>")
	s += ("</html>")
	return s

cgitb.enable()

form = cgi.FieldStorage()
name = form["name"].value
password = form['password'].value
signup_type = form['signup_type'].value
if signup_type not in ['register', 'login']:
	page = build_html_page("Signup type incorrectly specified.")
	print page
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
