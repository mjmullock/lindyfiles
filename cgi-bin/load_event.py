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
	s += ('<a href="../cgi-bin/home.py">Home</a>\t\t')
	s += ('<a href="../lindyfiles/message_board.html"> Go to the message board</a>\t\t')
	s += ('<a href="../cgi-bin/displayInfo.py"> View information</a>\n')	
 	s += ("<p>" + content_line + "\n")
 	s += ("</body>")
 	s += ("</html>")
 	return s

def format_table_results(res):
	t = '<table style="width:100%">' + '\n'
	for row in res:
		t+="<tr>"
		for element in row:
			t+="<td>" + str(element) + "</td> \n"
		t+="</tr> \n"
	t+="</table>"
	return t

def main():
	cgitb.enable()
	form = cgi.FieldStorage()
	event = form['eventName'].value

	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	cur = conn.cursor()
	cur.execute("SELECT * from events where name=?", (event,))
	res = c.fetchone()
	table = format_table_results(res)
	page = build_html_page(table)
	print page

if __name__ == "__main__":
	main()
