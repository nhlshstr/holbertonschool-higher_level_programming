#!/bin/bash
# takes a URL, sends request to that URL, displays size the body
curl -sI "$1" | awk '/Content-Length/{print $2}'
