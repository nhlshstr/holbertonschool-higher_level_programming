#!/usr/bin/python3
"""
displays the value of the X-Request-Id
"""

import urllib.request as httpreq
import sys

if __name__ == '__main__':
    with httpreq.urlopen(sys.argv[1]) as x:
        y = x.info()
        print(y.get("X-Request-Id"))
