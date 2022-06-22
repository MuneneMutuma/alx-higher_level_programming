#!/usr/bin/python3
"""A module that describes Square class with size attribute
"""


class Square:
    """This is an empty class for `Square`
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializer method for the class `Square`.

        Args:
            size: size of the square
                  size should be greater than or equal to zero
            position: coordinates of a square

        Raises:
            TypeError: if size is not an integer
                       if position is not a tuple of length 2
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Method to find area of a `Square` object

        Returns:
            int: area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """A method to retrieve size attr of the instance of `Square`

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter method to set the value of size for `Square`.

        Args:
            value: new value for size.

        Raises:
            TypeError: if `value` is not an integer.
            ValueError: if `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position attribute of square.

        Returns:
            tuple: position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function of the position attribute

        Args:
            value (tuple): must be of length 2. New value of position.
        """
        if not isinstance(value, tuple) or len(vale) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method to print the `Square` instance

        prints a square using #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                if self.__position[1] == 0:
                    print(" " * self.__position[0], end="")

                for i in range(self.__size):
                    print("#", end="")
                print("")
