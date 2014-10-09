#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
# instantiate a cookie here
name = form["name"].value

print "Content-Type: text/html"
#print c #the cookie
print
print "<html>"
print "<body>"
print "<h1>Hello, {}</h1>".format(name)
print "</body>"
print "</html>" 
