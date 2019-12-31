"""
Alex Petrov
CPE_202
Project 1
"""
class Node:
    """
    This class defines a node that has a value and another node as a direction
    """
    def __init__(self, first, next_node):
        """Defines Node class
        Args:
            first - an item that is stored in this node
            next - another node that this node is linked to

        Returns:
            This function does not return anything
        """
        self.first = first
        self.next = next_node

    def get_data(self):
        """
        """
        self.cur_data = self.first


class LinkedList:
    """
    This class defines a head that wraps around the node class.
    """
    def __init__(self):
        """Defines LinkedList class
        Args:
            head - a node that is initialized as part of the linked list

        Returns:
            This function does not return anything
        """
        self.head = Node(None, next_node = None)

    def get_head_data(self):
        """
        """
        self.data = self.head.first
