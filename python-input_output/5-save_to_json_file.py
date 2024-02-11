#!/usr/bin/python3
""" python input output """

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file
    using JSON
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
