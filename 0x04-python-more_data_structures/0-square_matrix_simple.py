#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return_list = []
    for i in matrix:
        sq_matrix = list(map(lambda x: x**2, i))
        return_list.append(sq_matrix)
    return return_list
