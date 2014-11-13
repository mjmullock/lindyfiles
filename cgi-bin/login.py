#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import os
import Cookie
import uuid
import datetime

import buildLoginForm
#import home

def build_html_page(content_line, cookie=None):
	s = ''
 	s += ("Content-Type: text/html\n")
 	if cookie is not None:
 		s += cookie.output(sep="\n")
 	s += ("\n\n<html>")
 	s += ("<body>")
 	s += ("<p>" + content_line + "\n")
 	s += ("</body>")
 	s += ("</html>")
 	return s
 
cgitb.enable()
 
form = cgi.FieldStorage()
signup_type = form['signup_type'].value
 

if signup_type not in ['register', 'login', 'logout']:
	print buildLoginForm.build_login_form("Signup type incorrectly specified.")
	exit(0)

#checking signup type first, to see if you should logout and not check for other form elements that wouldn't exist
if signup_type == "logout":
	oldc = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))
	if oldc is None:
		page = buildLoginForm.build_login_form('Error finding your current cookie. :(')
	else:
		c = Cookie.SimpleCookie()
		a = oldc['sessid']
		c['sessid'] = a
		c['sessid']['expires'] = 'Sun, 26 Oct 2014 00:00:01 GMT'
	page = buildLoginForm.build_login_form("You've successfully logged out", cookie=c)
	print page
	exit(0)
 
email = form['email'].value
password = form['password'].value


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
		expiration = datetime.datetime.now() + datetime.timedelta(days=30)
		#cookie['sessid']['expires'] = 'Sun, 23 Nov 2014 00:00:01 GMT'
		cookie['sessid']['expires'] = expiration.strftime("%a, %d %b %Y %H:%M:%S GMT")
	 	page = build_html_page("Welcome!", cookie)
		#home()
	else:
		page = buildLoginForm.build_login_form("Sorry, user " + email + " not found.")
		
else:
	if signup_type == 'register':
		page = buildLoginForm.build_login_form("Sorry, that name is already in use. Please choose another username.")
	elif len(res) != 1:
		page = buildLoginForm.build_login_form("Database consistency error, multiple results with the same name.")
	else:
		if password == res[0][1]:
			sessid = str(uuid.uuid4())
	 		ck = Cookie.SimpleCookie()
	 		ck['sessid'] = sessid 
			expiration = datetime.datetime.now() + datetime.timedelta(days=30)
			#cookie['sessid']['expires'] = 'Sun, 23 Nov 2014 00:00:01 GMT'
			ck['sessid']['expires'] = expiration.strftime("%a, %d %b %Y %H:%M:%S GMT")
			c.execute("update users set sessid = ? where email = ?", (sessid, email))
			conn.commit()
			page = build_html_page("Welcome back, " + email + ".", cookie=ck)
		else:
			page = buildLoginForm.build_login_form("Login error: incorrect password entered.")

c.close()
conn.close()
print page
exit(0)
