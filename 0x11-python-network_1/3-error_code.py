#!/usr/bin/python3
"""
Sends POST request with email
"""
import urllib.request as httpreq
import urllib.error as error
import sys


if __name__ == "__main__":
    try:
        with httpreq.urlopen(sys.argv[1]) as x:
            print(x.read().decode("utf-8"))
    except error.HTTPError as y:
        print("Error code: {}".format(y.code))
