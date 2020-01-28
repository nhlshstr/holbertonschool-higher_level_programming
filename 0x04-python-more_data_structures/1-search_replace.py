#!/usr/bin/python3
def search_replace(my_list, search, replace):
    your_list = my_list
    your_list = [
        x if not x == search else replace for x in my_list]
    return your_list
