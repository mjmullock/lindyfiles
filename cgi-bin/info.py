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
 	s += ("<p>" + content_line + "\n")
 	s += ("</body>")
 	s += ("</html>")
 	return s

#takes name of table (string) from lindyfiles.db and returns list of comma-separated strings with all results
def retrieve_all_results_from_table(table):
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	c = conn.cursor()
	c.execute("SELECT * from ?", table)
	res = c.fetchall()
	c.close()
	conn.close()
	return res
	

#takes a list of strings that are the results from a table, then 
def format_table_results(res):
	for row in res:
		print row


gitb.enable()

res = retrieve_all_results_from_table("events")
format_table_results(res)



