#!/usr/bin/python3
"""Defines a square with size attribute """


class Square:
    """
    This class defines a square by encapsulating the size and position as private instance attributes.

    The square is characterized by having all sides of equal length.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class with optional size and position parameters.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
          Raises:
          - TypeError: If size is not an integer.
          - ValueError: If size is less than 0.
        - position (tuple, optional): The position of the square. Default is (0, 0).
          Raises:
          - TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout, considering the position.

        If size is equal to 0, prints an empty line.
        If position[1] > 0, spaces are used to align the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        This method provides a human-readable string that represents the
        Square object. It is useful for debugging and informative purposes.
        """
        return f"Square with size: {self.__size}, position: {self.__position}"

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value (int): The new size of the square.
          Raises:
          - TypeError: If value is not an integer.
          - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Parameters:
        - value (tuple): The new position of the square.
          Raises:
          - TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
