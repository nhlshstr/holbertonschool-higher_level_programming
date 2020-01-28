#!/usr/bin/python3
common_set = []


def common_elements(set_1, set_2):
    for i in set_1:
        for j in set_2:
            if i == j:
                common_set.append(j)
    return common_set
