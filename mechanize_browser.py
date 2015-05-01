#!/usr/bin/env
import mechanize
import cookielib


def test_agent(url, user_agent):
    browser = mechanize.Browser()
    browser.addheaders = user_agent
    page = browser.open(url)
    source_code = page.read()
    print source_code


def print_cookies(url):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    for cookie in cookie_jar:
        print cookie


user_agent = [('User-agent', 'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')]
url = 'http://www.jwarren.co/http/'

test_agent(url, user_agent)
print_cookies(url)
