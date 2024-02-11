#!/usr/bin/python3
""" python input output """

import json


def load_from_json_file(filename):
    """
    function that creates an object
    from a JSON FILE
    """

    with open(filename, "r") as f:
        return json.load(f)
