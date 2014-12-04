
def build_html_page(content_line, cookie=None):
	s = ''
	s += ("Content-Type: text/html\n")
	if cookie is not None:
		s += cookie.output()
	s += ("\n\n<html>")
	s += ("<body>")
	s += ('<a href="../cgi-bin/home.py">Home</a>\t\t')
	s += ('<a href="../lindyfiles/profile.html"> Profile</a>\t\t')
	s += ('<a href="../lindyfiles/query_screen.html"> View information</a>\n')	
	s += ("<p>" + content_line + "\n")
	s += ("<FORM METHOD=GET ACTION='./login.py'>\n")
	s += ("<input type='hidden' name='signup_type' value='logout'>\n")
	s += ("<p> <INPUT TYPE=submit value='logout'>\n")
	s += ("</FORM>\n")
	s += ("</body>")
	s += ("</html>")
	return s

if __name__=='__main__':
    print build_html_page(content_line, cookie=None)
