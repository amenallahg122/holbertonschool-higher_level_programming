#!/usr/bin/python3
"""
base class
"""

import json


class Base:
    """
    base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

        """
        Dictionary to JSON string
        """

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns returns the
        JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    """
    JSON string to file
    """

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that writes the JSON string
        representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        list_dic = []

        if list_objs is None:
            with open(filename, "w") as f:
                f.write(cls.to_json_string(list_dic))
            return
        for obj in list_objs:
            list_dic.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dic))

    """
    JSON string to dictionary
    """

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of the
        JSON string representation json_string
        """

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    """
    Dictionary to Instance
    """

    @classmethod
    def create(cls, **dictionary):
        """
        method that returns an instance
        with all attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    """
    File to instances
    """

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances:
        """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as f:
                lis_obj = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in lis_obj]
        except FileNotFoundError:
            return []
