#!/usr/bin/python3
"""
class square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square tht inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

        """
        setter and getter
        """

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

        """
        update
        """

    def update(self, *args, **kwargs):
        """
        method that assigns attributes
        """

        if args and len(args) != 0:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                elif idx == 1:
                    self.size = args[idx]
                elif idx == 2:
                    self.x = args[idx]
                elif idx == 3:
                    self.y = args[idx]
        else:
            if len(kwargs) > 0:
                key = kwargs.keys()
                for i in key:
                    if i == "id":
                        self.id = kwargs["id"]
                    elif i == "size":
                        self.size = kwargs["size"]
                    elif i == "x":
                        self.x = kwargs["x"]
                    elif i == "y":
                        self.y = kwargs["y"]

            """
            instance to dictionary
            """

    def to_dictionary(self):
        """
        that returns the dictionary representation of a Square
        """

        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
