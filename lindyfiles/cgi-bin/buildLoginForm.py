
def build_login_form(cookie=None):
	s = ''
	s += ("Content-Type: text/html\n")
	if cookie is not None:
		print cookie
	s += ("\n<html>\n")
	s += ("<body>\n")
	s += ("If this is your first time on the site please sign up with your email and password\n")
	s += ("<FORM METHOD=GET ACTION='../cgi-bin/login.py'>\n")
	s += ("email: <input name='email' size=10 maxlength=50>\n")
	s += ("password: <input name='password' size=10 maxlength=15>\n")
	s += ("<input type='hidden' name='signup_type' value='register'>\n")
	s += ("<p> <INPUT TYPE=submit value='sign up'>\n")
	s += ("</FORM>\n")
	s += ("If you have already created an account please log in\n")
	s += ("<FORM METHOD=GET ACTION='../cgi-bin/login.py'>\n")
	s += ("email: <input name='email' size=10 maxlength=50>\n")
	s += ("password: <input name='password' size=10 maxlength=15>\n")
	s += ("<input type='hidden' name='signup_type' value='login'>\n")
	s += ("<p> <INPUT TYPE=submit value='login'>\n")
	s += ("</FORM>\n")
	s += ("</body>\n")
	s += ("</html>\n")
	return s

if __name__=='__main__':
    print build_login_form(cookie=None)
