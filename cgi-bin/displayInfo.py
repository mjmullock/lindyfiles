#!/usr/bin/python

def header():
	print "Content-type: text/html\n\n"

header()

print "<html><body>"
print "<h2>Please choose a table to view</h2>"
print "<FORM METHOD=GET ACTION='./info.py'>\n"
print "<select name = 'table'>"
print "<option value = 'pros'></option>"
print "<option value = 'events'</option>"
print "<p> <INPUT TYPE=submit value='select'>\n"
print "</FORM>\n"
print "</body></html>"
