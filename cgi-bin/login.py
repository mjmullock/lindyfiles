#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import os
import Cookie
import uuid

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
 
# cookie_string = os.environ.get('HTTP_COOKIE')
# if cookie_string:
# 	try:
# 		c = Cookie.SimpleCookie(cookie_string)
# 		print build_html_page("sessid: " + c["sessid"].value)
# 		exit(0)
# 	except:
# 		c = Cookie.SimpleCookie()
# 		c['sessid'] = 'test_cookie'
# 		print build_html_page("Building cookie...", cookie=c)
# 		exit(0)
# else:
# 	c = Cookie.SimpleCookie()
# 	c['sessid'] = 'test_cookie'
# 	print build_html_page("Building cookie...", cookie=c)
# 	exit(0)
    
# c = Cookie.SimpleCookie()
# c['sessid'] = uuid.uuid1()

form = cgi.FieldStorage()
# print "Content-type: text/html\n"
# print "Set-Cookie: sessid=18340592-5bc6-11e4-874d-deadbe099100\n\n" 
# print "<html><body>"
email = form['email'].value
password = form['password'].value
signup_type = form['signup_type'].value
logout = form['logout'].value
# print email + ", " + password + ", " + signup_type 
# print "</body></html>"
# print build_html_page("Building cookie...", cookie=c)
# exit(0)
# email = form['email'].value
# name = form["name"].value
# password = form['password'].value
# signup_type = form['signup_type'].value
if signup_type not in ['register', 'login']:
	print build_html_page("Signup type incorrectly specified.")
	exit(0)


conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
c = conn.cursor()
c.execute("select * from users where email = ?", (email,))
res = c.fetchall()

if not len(res):
	if signup_type == 'register':
		sessid = str(uuid.uuid4())
		c.execute("insert into users (email, password, sessid) values(?,?,?);", (email, password, sessid))
		conn.commit()
	 	cookie = Cookie.SimpleCookie()
	 	cookie['sessid'] = sessid 
	 	page = build_html_page("Welcome!", cookie)
#		page = build_html_page("Welcome, " + name)
	else:
		page = build_html_page("Sorry, user '" + email + "' not found.")
else:
	if signup_type == 'register':
		page = build_html_page("Sorry, that name is already in use.")
	elif len(res) != 1:
		page = build_html_page("Database consistency error, multiple results with the same name")
	else if logout == 'true':
		ck = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
		ck2 = Cookie.SimpleCookie()
		ck2['sessid'] = ck['sessid']
		ck2['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	else:
		if password == res[0][1]:
			sessid = str(uuid.uuid4())
	 		ck = Cookie.SimpleCookie()
	 		ck['sessid'] = sessid 
			c.execute("update users set sessid = ? where email = ?", (sessid, email))
			conn.commit()
			page = build_html_page("Welcome back, " + email + ".", cookie=ck)
		else:
			page = build_html_page("Login error: incorrect password entered.")

print page
exit(0)
