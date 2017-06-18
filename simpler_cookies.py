#! /Python35/python
from http import cookies
import os

class simpler_cookies(object):
    """Class to handle cgi cookies because they are crap"""
    def __init__(self):
        super(simpler_cookies, self).__init__()
        self.cookies = cookies.SimpleCookie()
        cookie_string = os.environ.get('HTTP_COOKIE')
        self.cookies.load(cookie_string)


    # returns cookie content matching name string if present, otherwise returns empty str
    def get_cookie(self, name):
        name = str(name)
        if name in self.cookies:
            # cookie exists
            return self.cookies[name].value
        else:
            # cookie doesnt exist
            return ""


    # returns cookie contents as tuple corresponding to those passed in
    # cookies that dont exist returned as empty string
    def get_cookies(self, names):
        return_value = []
        for name in names:
            if name in self.cookies:
                # cookie exists
                return_value.append(self.cookies[name].value)
            else:
                # cookie doesnt exist
                return_value.append("")
        return tuple(return_value)


    # returns True where all cookies exist
    # otherwise returns false
    def all_cookies_exist(self, names):
        for name in names:
            if name not in self.cookies:
                # cookie doesnt exist
                return False
        return True


# Purpose: Function to test the functionality of the class.
def main():
    return

if __name__ == '__main__':
    main()
