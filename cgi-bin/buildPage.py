
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

if __name__=='__main__':
    print build_html_page(content_line, cookie=None)
