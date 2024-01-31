#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lista = []
    for row in matrix:
        lista.append(list(map(lambda num: num**2, row)))
    return (lista)
