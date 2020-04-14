#!/usr/bin/python3
"""
Gets body of site
"""

import requests


if __name__ == "__main__":
    a = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(a.text), a.text))
