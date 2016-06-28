# Allows you to browse through the given url and submit forms
import mechanize
import webbrowser
# Initialize Browser object
br = mechanize.Browser()

# Save current session and use it for later
c = mechanize.CookieJar()
br.set_cookiejar(c)

# Ignore robots.txt to login to a website
br.set_handle_robots(False)

# Open the website you are trying to log in to
br.open("http://signin.gmarket.co.kr/LogIn/LogIn")

# Specify the id of the form to be submitted
br.select_form("defaultForm")
# name of the inputs = id/password
br.form['id'] = "you wish"
br.form['pwd'] = "you knew"
# Submit!
r = br.submit()

# Returns html file of the resulting page
print r.read()





