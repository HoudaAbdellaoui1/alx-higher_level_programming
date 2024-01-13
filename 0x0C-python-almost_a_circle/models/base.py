#!/usr/bin/python3
"""Defines a Base class """


class Base:
    """
    This class defines a base

    Attributes:
        __nb_objects (int): The number of objects.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class with optional ID.

        Parameters:
        - id (int, optional): identifier attribute.
        """
        if id is not None:
            self.id = id
        else:
            type(self).number_of_instances += 1
            self.id = type(self).number_of_instances

    @property
    def id(self):
        """
        Getter method for the id attribute.

        Returns:
        - id: The identifier of the base instance.
        """
        return self.__nb_objects

    @id.setter
    def id(self, value):
        """
        Setter method for the id attribute.

        Parameters:
        - value (int): The new value of the id.
        """

        self.id = value
