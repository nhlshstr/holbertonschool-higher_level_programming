#!/usr/bin/python3
"""
Script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    input_var = "" if len(sys.argv) == 1 else sys.argv[1]

    post_req = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": input_var})
    try:
        json_post_req = post_req.json()
        if json_post_req != {}:
            print("[{}] {}".format(json_post_req.get("id"),
                                   json_post_req.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
