#!/usr/bin/python3
"""
Gets the body of the Holberton page
"""

import urllib.request as httpreq

if __name__ == '__main__':
    with httpreq.urlopen("https://intranet.hbtn.io/status") as x:
        y = x.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".format(type(y), y, y.decode("utf-8")))
