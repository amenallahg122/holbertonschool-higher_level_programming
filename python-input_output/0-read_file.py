#!/usr/bin/python3
""" read a file """


def read_file(filename=""):
    """function that reads a text file UTF8"""

    with open(filename, encoding="utf-8") as filename:
        print(filename.read(), end="")
