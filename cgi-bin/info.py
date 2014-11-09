#!/usr/bin/python

import cgi
import cgitb
import sqlite3

def build_html_page(content_line, cookie=None):
	s = ''
 	s += ("Content-Type: text/html\n")
 	if cookie is not None:
                print cookie
 	s += ("\n<html>")
 	s += ("<body>")
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


cgitb.enable()

form = cgi.FieldStorage()
selected_table = form['table'].value

res = retrieve_all_results_from_table(selected_table)
table = format_table_results(res)
page = build_html_page(table)
print page




