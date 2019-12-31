"""
Alex Petrov
CPE_202
Project 1
"""
class Node:
    """
    This class defines a node that has a value and another node as a direction
    """
    def __init__(self, data, next_node=None):
        """Defines Node class
        Args:
            first - an item that is stored in this node
            next - another node that this node is linked to

        Returns:
            This function does not return anything
        """
        self.data = data
        self.next = next_node

    def __repr__(self):
        return "Node(key/data:%s, next:%s)"\
         % (self.data, self.next)

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
        self.head = Node(None)

    def get_head_data(self):
        """
        """
        self.data = self.head.first
n1 = Node(("smort", "smort"))
print(n1.data[0])
