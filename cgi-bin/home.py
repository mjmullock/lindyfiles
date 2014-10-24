#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import os
import Cookie
import uuid
import buildPage
import buildLoginForm

# create database connection
# conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
# cur = conn.cursor()

# check for cookie
# cookie_string = os.environ.get('HTTP_COOKIE')

# if there is a cookie
# if cookie_string:
# 
#     # look in database for user with that sessid
#     cookie = Cookie.SimpleCookie(cookie_string)
#     sessid = cookie["sessid"]   
#     cur.execute("SELECT fname FROM users WHERE sessid = ?", sessid) 
#     results = cur.fetchone()
#     if results:
#         name = results[0]
buildPage.build_html_page("Welcome back, " + name) 
#     else:
#         buildPage.build_html_page("Cookie found but user not found")

# if no cookie show register/login option
# else:

    # show login/register options
 #   buildLoginForm.build_login_form() 
 
#    # if register:
#    cookie = Cookie.SimpleCookie()
#    cookie["sessid"] = uuid.uuid1()
#    buildLoginForm.build_login_form(cookie) 
#
#        # if db doesn't already contain email: put their info in db along with new sessid, 
#        # give user cookie w/ that sessid
#        
#
#        # if db does already contain email: say sorry, email already in use
# 
#    # if login: validate info from db
#
#        # if db does contain correct info: add or replace sessid with a new one
#        # give user cookie w/ that sessid
#
# close db connection
# cur.close()
# conn.close()


