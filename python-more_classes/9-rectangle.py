#!/usr/bin/python3
"""Rectangle."""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

        """ Private instance width """

    @property
    def width(self):
        """with of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        """ Private instance height """

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        """Public instance method calulate area"""

    def area(self):
        """area rectangle"""
        return self.__width * self.__height

        """Public instance method calculte perimetre"""

    def perimeter(self):
        """perimetre rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """string represent the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    """print messsage when an instance Rectangle is deleted"""

    def __del__(self):
        Rectangle.number_of_instances -= 1
        """delete"""
        print("Bye rectangle...")

        """static method biggest or qual """

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger or equal method"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

        """class method"""

    @classmethod
    def square(cls, size=0):
        """return new rctangle with <idth=height=size"""

        return cls(size, size)
