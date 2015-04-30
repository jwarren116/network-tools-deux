#!/usr/bin/env
import mechanize


def test_agent(url, user_agent):
    browser = mechanize.Browser()
    browser.addheaders = user_agent
    page = browser.open(url)
    source_code = page.read()
    print source_code

user_agent = [('User-agent','Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')]
url = 'http://whatsmyuseragent.com/'

test_agent(url, user_agent)
