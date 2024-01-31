#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list = []
    for i in matrix:
        list.append(list(map(lambda x: x**2, i)))
    return list
