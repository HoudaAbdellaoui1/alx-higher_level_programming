#!/usr/bin/python3
class Node:
    """
    This class defines a node of a singly linked list.

    Each node has a data attribute and a reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class with data and next_node parameters.

        Parameters:
        - data (int): The data to be stored in the node. Must be an integer.
          Raises:
          - TypeError: If data is not an integer.
        - next_node (Node, optional): The next node in the list. Default is None.
          Raises:
          - TypeError: If next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
        - int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Parameters:
        - value (int): The new data to be stored in the node.
          Raises:
          - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
        - Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Parameters:
        - value (Node): The new next node in the list.
          Raises:
          - TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.

    The list consists of nodes, each containing an integer data value.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.

        The list is initially empty.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Parameters:
        - value (int): The data to be stored in the new node.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the SinglyLinkedList object.

        This method prints the entire list in stdout, one node number per line.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
