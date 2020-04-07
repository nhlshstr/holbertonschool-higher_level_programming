#!/bin/bash
#  takes in a URL and displays all HTTP methods
curl -sI "$1" | awk '/Allow/' | cut -d' ' -f2-
