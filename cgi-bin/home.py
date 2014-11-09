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


# ck = Cookie.SimpleCookie(cookie_string)
# sessid = ck["sessid"].value   
# cur.execute("SELECT email FROM users WHERE sessid = ?", (sessid,)) 
# results = cur.fetchone()
# email = results[0]
# # s = "sessid: " + sessid + ", email: " + email 
# s = "Welcome back, " + email
# print buildPage.build_html_page(s) 
# cur.close()
# conn.close()
# exit(0)

# if there is a cookie
if cookie_string:
 
	# look in database for user with that sessid
	try:
		ck = Cookie.SimpleCookie(cookie_string)
		sessid = ck["sessid"].value   
		cur.execute("SELECT email FROM users WHERE sessid = ?", (sessid,)) 
		results = cur.fetchone()
		email = results[0]
		print buildPage.build_html_page('<a href="../lindyfiles/message_board.html"> Go to the message board</a><p><p>\t' + '<a href="../cgi-bin/displayInfo.py"> View information</a>\n' +	"Welcome back, " + email) 
	except:
		# print buildPage.build_html_page("Cookie found but user not found. sessid = " + cookie["sessid"].value)
		print buildLoginForm.build_login_form() 
# if no cookie show register/login option
else:

	# show login/register options
	print buildLoginForm.build_login_form() 
 
	# if register:
#	cookie = Cookie.SimpleCookie()
#	cookie["sessid"] = uuid.uuid1()
#	buildLoginForm.build_login_form(cookie) 
	
	    # if db doesn't already contain email: put their info in db along with new sessid, 
	    # give user cookie w/ that sessid
	    
	
	    # if db does already contain email: say sorry, email already in use
	
	# if login: validate info from db
	
	    # if db does contain correct info: add or replace sessid with a new one
	    # give user cookie w/ that sessid

# close db connection
cur.close()
conn.close()


