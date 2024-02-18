#!/usr/bin/python3
"""
class rectangle
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area
        """
        return self.__width * self.__height

    def display(self):
        """
        display
        """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width + self.__x):
                if j < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Update
        """
        if args and len(args) != 0:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                elif idx == 1:
                    self.__width = args[idx]
                elif idx == 2:
                    self.__height = args[idx]
                elif idx == 3:
                    self.__x = args[idx]
                elif idx == 4:
                    self.__y = args[idx]
        else:
            if len(kwargs) > 0:
                key = kwargs.keys()
                for i in key:
                    if i == "id":
                        self.id = kwargs["id"]
                    elif i == "width":
                        self.__width = kwargs["width"]

                    elif i == "height":
                        self.__height = kwargs["height"]
                    elif i == "x":
                        self.__x = kwargs["x"]
                    elif i == "y":
                        self.__y = kwargs["y"]

    def to_dictionary(self):
        """
        dictionary reprentation of a rectangle
        """

        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
