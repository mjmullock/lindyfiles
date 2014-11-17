#!/usr/bin/python

import cgi
import cgitb
import sqlite3


def tabular(arr):
	s = ""
	for i in xrange(len(arr) - 1):
		s += arr[i] + '\t'
	s += arr[len(arr)-1]
	return s

def main():
	cgitb.enable()
	form = cgi.FieldStorage()
	eventID = form['event'].value
	
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	cur = conn.cursor()
	cur.execute("SELECT * from events where eventID=?", (eventID,))
	res = c.fetchone()
	print tabular(res)
