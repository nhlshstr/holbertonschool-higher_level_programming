#!/usr/bin/python3
"""
Script that takes in a URL,
sends a request to the URL
and displays the body of the
response.
"""

import requests
import sys

if __name__ == "__main__":
    if requests.get(sys.argv[1]).status_code >= 400:
        print("Error code: {}".format(requests.get(sys.argv[1]).status_code))
    else:
        print(requests.get(sys.argv[1]).text)
