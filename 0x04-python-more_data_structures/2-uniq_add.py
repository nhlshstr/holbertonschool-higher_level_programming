#!/usr/bin/python3
def uniq_add(my_list=[]):
    su_m = 0
    my_set = set(my_list)
    for i in my_set:
        su_m += i
    return su_m
