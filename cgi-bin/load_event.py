#!/usr/bin/python

import cgi
import cgitb
import sqlite3


def tabular(arr):
	s = ""
	for i in xrange(len(arr) - 1):
		s += str(arr[i]) + '\t'
	s += str(arr[len(arr)-1])
	return s

def main():
	cgitb.enable()
	form = cgi.FieldStorage()
	try:
		eventID = int(form['event'].value)
	except KeyError:
		eventID = 2
	
	conn = sqlite3.connect('/home2/mmullock/public_html/lindyfiles/lindyfiles.db')
	cur = conn.cursor()
	cur.execute("SELECT * from events where id=?", (eventID,))
	res = cur.fetchone()
	cur.close()
	conn.close()
	
	print "Content-type: text/html"
	print
	print tabular(res)

if __name__ == "__main__":
	main()
