#!/usr/bin/python

def header():
	print "Content-type: text/html\n\n"

header()

print "<html><body>"
print '<a href="../cgi-bin/home.py">Home</a>\t\t'
print '<a href="../lindyfiles/message_board.html"> Go to the message board</a>\n'
print "<h2>Please choose a table to view</h2>"
print "<FORM METHOD=GET ACTION='./info.py'>\n"
print "<select name = 'table'>"
print "<option value = 'pros'>Pros</option>"
print "<option value = 'events'>Events</option>"
print "</select>"
print "<p> <INPUT TYPE=submit value='select'>\n"
print "</FORM>\n"
print "</body></html>"
