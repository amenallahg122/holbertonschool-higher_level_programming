#!/usr/bin/python3
"""python input output"""


def pascal_triangle(n):
    """a function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascal’s triangle of n"""
    pascal = []
    if n <= 0:
        return pascal
    else:
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                elif i >= 2:
                    row.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
            pascal.append(row)
    return pascal
