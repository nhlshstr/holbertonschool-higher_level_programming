#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Class for rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area"""
        return self.height * self.width

    def display(self):
        """Prints rectangle"""
        for vert in range(self.y):
            print("")
        for y in range(self.height):
            for hor in range(self.x):
                print(" ", end="")
            for x in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        if len(args) != 0 and args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
            return
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def __str__(self):
        """Str override"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, num):
        """Setter for height"""
        if type(num) is not int:
            raise TypeError("height must be an integer")
        if num <= 0:
            raise ValueError("height must be > 0")
        self.__height = num

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, num):
        """Setter for width"""
        if type(num) is not int:
            raise TypeError("width must be an integer")
        if num <= 0:
            raise ValueError("width must be > 0")
        self.__width = num

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, num):
        """Setter for x"""
        if type(num) is not int:
            raise TypeError("x must be an integer")
        if num < 0:
            raise ValueError("x must be >= 0")
        self.__x = num

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, num):
        """Setter for y"""
        if type(num) is not int:
            raise TypeError("y must be an integer")
        if num < 0:
            raise ValueError("y must be >= 0")
        self.__y = num
