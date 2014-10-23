
def build_login_form(cookie=None):
	s = ''
	s += ("Content-Type: text/html\n")
	if cookie is not None:
		print cookie
	s += ("\n<html>")
	s += ("<body>")
	s += ("If this is your first time on the site please sign up with your email and password")
	s += ("<FORM METHOD=GET ACTION='../cgi-bin/login.py'>")
	s += ("email: <input name='email' size=10 maxlength=50>")
	s += ("password: <input name='password' size=10 maxlength=15>")
	s += ("<input type='hidden' name='signup_type' value='register'>")
	s += ("<p> <INPUT TYPE=submit value='sign up'>")
	s += ("</FORM>")
	s += ("If you have already created an account please log in")
	s += ("<FORM METHOD=GET ACTION='../cgi-bin/login.py'>")
	s += ("email: <input name='email' size=10 maxlength=50>")
	s += ("password: <input name='password' size=10 maxlength=15>")
	s += ("<input type='hidden' name='signup_type' value='login'>")
	s += ("<p> <INPUT TYPE=submit value='login'>")
	s += ("</FORM>")
	s += ("</body>")
	s += ("</html>")
	return s

if __name__=='__main__':
    print build_html_page(cookie=None)
