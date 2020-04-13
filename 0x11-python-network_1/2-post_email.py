#!/usr/bin/python3
"""
Sends POST request with email
"""
import urllib.request as httpreq
import sys
import urllib.parse as parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    parseD = parse.urlencode({"email": email}).encode("ascii")
    x = httpreq.Request(url, parseD)
    with httpreq.urlopen(x) as y:
        print(y.read().decode("utf-8"))
