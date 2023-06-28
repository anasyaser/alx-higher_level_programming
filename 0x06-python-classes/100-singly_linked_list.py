#!/usr/bin/python3
"""Singly linked list of integers"""


class Node:
    """
    Represent Node of singly linked list

    Args:
        data: Node data
        next_node: next node of current node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter attribute: data"""
        return self.__data

    @property.setter
    def data(self, value):
        """
        Setter attribute: data

        Args:
            value: data value
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter attribute: next_node"""
        return self.__node

    @property.setter
    def next_node(self, value):
        """
        Setter attribute: next_node

        Args:
            value: next node value
        """
        if isinstance(value, Node):
            self.__next = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """
    Represent singly linked list

    Attributes:
        head: head of linked list
    """

    def __init__():
        self.__head = None

    def insert_end(self, data):
        """
        Insert node to the end of linked list

        Args:
            data: data of added node
        """

        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
        else:
            current = self.__head
            while(current.next_node):
                current = current.next_node

            current.next_node = new_node

    def sorted_insert(self, data):
        """
        Insert node to linked list in sorted position (increasing order)

        Args:
            data: data of added node
        """

        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
        else:
            current = self.__head
