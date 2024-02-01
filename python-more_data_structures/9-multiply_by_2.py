#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    for key in a.keys():
        a[key] *= 2
    return (a)
