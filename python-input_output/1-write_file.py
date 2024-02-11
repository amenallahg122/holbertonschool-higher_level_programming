#!/usr/bin/python3
""" write a file using with """


def write_file(filename="", text=""):
    """function that write a string to a text file UTF8"""

    with open(filename, "w", encoding="utf-8") as filename:
        return filename.write(text)
