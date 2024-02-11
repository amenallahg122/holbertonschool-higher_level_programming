#!/usr/bin/python3
""" write a file using with """

import json


def to_json_string(my_obj):
    """
    function that  return the JSON  representation of an object string
    """
    return json.dumps(my_obj)
