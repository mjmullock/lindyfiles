#!/usr/bin/python

import cgi
import cgitb
import sqlite3
from queries import get_nearby_events
from queries import get_upcoming_events

def build_html_page(content_line, cookie=None):
	s = ''
	s += ("Content-Type: text/html\n")
	if cookie is not None:
				print cookie
	s += ("\n<html>")
	s += ("<body>")
	s += ('<a href="../cgi-bin/home.py">Home</a>\t\t')
	s += ('<a href="../lindyfiles/message_board.html"> Go to the message board</a>\t\t')
	s += ('<a href="../cgi-bin/displayInfo.py"> View information</a>\n')	
	s += ("<p>" + content_line + "\n")
	s += ("</body>")
	s += ("</html>")
	return s

#takes name of table (string) from lindyfiles.db and returns list of comma-separated tuples with all results
def retrieve_all_results_from_table(table):
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	c = conn.cursor()
	
	if table == "events":
		c.execute("SELECT * from events")
	elif table == "pros":
		c.execute("SELECT * from pros")

	res = c.fetchall()
	c.close()
	conn.close()
	return res
	

#takes a list of tuples that are the results from a table, then 
def format_table_results(res):
	t = '<table style="width:100%">' + '\n'
	for row in res:
		t+="<tr>"
		for element in row:
			t+="<td>" + str(element) + "</td> \n"
		t+="</tr> \n"
	t+="</table>"
	return t

def show_event_links(res):
	t = '<table style="width:100%">' + '\n'
	for row in res:
		t += "<tr>"
		eventID = str(row[0])
		name = str(row[1])
		if name == "Event Name":
			continue
		t += "<a href='../lindyfiles/event_template.html?eventID=" + eventID + "'> " + name + " </a>"
		t += "</tr> <p> \n"
	t += "</table>"
	return t

cgitb.enable()

form = cgi.FieldStorage()
selected_table = form['table'].value
#if selected_table == 'upcoming_events':
city = form['city'].value
state = form['state'].value

if selected_table == "pros":
	res = retrieve_all_results_from_table(selected_table)
	table = format_table_results(res)
elif selected_table == "all_events":
	res = retrieve_all_results_from_table(selected_table)
	table = show_event_links(res)
elif selected_table == "nearby_events":
	table = format_table_results(get_nearby_events(city, state))
elif selected_table == "upcoming_events":
	table = format_table_results(get_upcoming_events()) 
	# table = format_table_results(res)
# page = build_html_page(table)
# print page
print "Content-type: text/html"
print
print table
