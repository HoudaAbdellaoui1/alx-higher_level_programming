#!/usr/bin/python3
""" My list module """

class MyList(list):
    """ MyList class inherits from the built-in list class and adds a print_sorted method."""
    def print_sorted(self):
        """ Prints the list in ascending order."""
        print(sorted(self.copy()))
