#!/usr/bin/python

def build_html_page(content_line, cookie=None):
	s = ''
	s += ("Content-Type: text/html\n")
	s += ("\n<html>")
	s += ("<body>")
	s += ("<p>" + content_line + "\n")
	s += ("</body>")
	s += ("</html>")
	return s 

print build_html_page("Hello")

