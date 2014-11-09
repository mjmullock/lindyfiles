
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
	s += ("<FORM METHOD=GET ACTION='./logout.py'>\n")
	s += ("<input type='hidden' name='logout' value='true'>\n")
	s += ("<p> <INPUT TYPE=submit value='logout'>\n")
	s += ("</FORM>\n")
	s += ("</body>")
	s += ("</html>")
	return s

if __name__=='__main__':
    print build_html_page(content_line, cookie=None)
