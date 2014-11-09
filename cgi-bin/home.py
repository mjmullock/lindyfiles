#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import os
import Cookie
import uuid

import buildPage
import buildLoginForm

cgitb.enable()

# create database connection
conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
cur = conn.cursor()

# check for cookie
cookie_string = os.environ.get('HTTP_COOKIE')


# if there is a cookie
if cookie_string:
 
	# look in database for user with that sessid
	try:
		ck = Cookie.SimpleCookie(cookie_string)
		sessid = ck["sessid"].value   
		cur.execute("SELECT email FROM users WHERE sessid = ?", (sessid,)) 
		results = cur.fetchone()
		email = results[0]
		print buildPage.build_html_page("Welcome back, " + email) 
	except:
		# print buildPage.build_html_page("Cookie found but user not found. sessid = " + cookie["sessid"].value)
		print buildLoginForm.build_login_form("") 
# if no cookie show register/login option
else:

	# show login/register options
	print buildLoginForm.build_login_form("") 
 

# close db connection
cur.close()
conn.close()


