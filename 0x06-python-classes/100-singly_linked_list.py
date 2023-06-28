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

    @data.setter
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
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter attribute: next_node

        Args:
            value: next node value
        """
        if (value is None) or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Represent singly linked list

    Attributes:
        head: head of linked list
    """

    def __init__(self):
        self.__head = None

    def insert_between(self, prev_node, next_node, new_node):
        """
        insert node between another two's

        Args:
           prev_node: (Node) previous node
           next_node: (Node) next node
           new_node: (Node) new added node
        """
        if prev_node is not None:
            prev_node.next_node = new_node
        else:
            self.__head = new_node
        new_node.next_node = next_node

    def sorted_insert(self, data):
        """
        Insert node to linked list in sorted position (increasing order)

        Args:
            data: data of added node
        """

        new_node = Node(data)

        if self.__head is None:
            self.__head = new_node
        else:
            prev = None
            current = self.__head

            while(current):
                if new_node.data < current.data:
                    self.insert_between(prev, current, new_node)
                    return
                prev = current
                current = current.next_node
            prev.next_node = new_node

    def __str__(self):
        nodes = []
        current = self.__head
        while(current):
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
