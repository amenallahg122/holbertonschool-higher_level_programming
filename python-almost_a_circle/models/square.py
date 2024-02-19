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

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

            """
            instance to dictionary
            """

    def to_dictionary(self):
        """
        that returns the dictionary representation of a Square
        """

        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
