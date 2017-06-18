#! /Python35/python
import cgi
import cgitb # use for error traces - disable for Hard Mode
from http import cookies

# comment out following line when not in testing to hide failures
cgitb.enable()

"""
Purpose: class to try and simplify the cgi response process
         because CGI is the antichrist.
         Also learning how to use classes in python
"""


class response(object):
    """Handler for building cgi responses because they are shit"""
    def __init__(self):
        # autogen, not neccessary but good for when inheriting, safe to delete
        super(response, self).__init__()

        # vars for normal use
        self.raw_html = ""
        self.cookie = cookies.SimpleCookie()
        self.cookie_flag = False
        self.html_flag = False
        self.redirect_flag = False
        self.redirect_address = ""


    # adds html to the response
    def set_html_response(self, raw_html):
        self.raw_html = str(raw_html)
        self.html_flag = True


    # overrides any cookie set via the easy cookie append method or
    # the easy cookie delete methods
    # and may cause errors if used improperly
    def set_cookie(self, simple_cookie):
        self.cookie = simple_cookie
        self.cookie_flag = True


    # applies a redirect to headers, useful for cookie setting scripts
    def set_redirect(self, redirect_address):
        self.redirect_address = str(redirect_address)
        self.redirect_flag = True


    # appends cookie to current response
    # uses default parameters for other items
    def easy_append_cookie(self, cookie_name, cookie_str):
        self.cookie[str(cookie_name)] = str(cookie_str)
        self.cookie_flag = True


    # sets cookie on client machine to expire
    def easy_delete_cookie(self, cookie_name):
        self.cookie[str(cookie_name)] = ""
        self.cookie[str(cookie_name)]['expires'] = 0


    # prints response generated
    def send_response(self):
        #send cookie
        if self.cookie_flag is True:
            print(self.cookie)
        # redirect if necessary
        if self.redirect_flag is True:
            print("Location: " + self.redirect_address + "\r\n")
        # send content header
        print('Content-Type: text/html\r\n')
        # send rest of webpage
        print(self.raw_html)


# prints simple set of test data
def main():
    ires = response()
    ires.set_html_response("<html>you are being redirected</html>")
    # uncomment to test redirect
    # ires.set_redirect("cookie_exp.py")
    ires.easy_delete_cookie("user")
    ires.send_response()

if __name__ == '__main__':
    main()
