"""
Alex Petrov
CPE 202
Project 1
"""
from linked import LinkedList
from linked import Node

class StackArray:
    """This class defines a stack that is built out of an array
    """
    def __init__(self, capacity):
        """This function initializes the stack

        Args:
            capacity(int) - this is an integer value that says how many
            items the list will be able to hold

            num_items(int) - this integer keeps track of how many items
            (that are not None) are in the array

            items(list) - this is a list that is initialized as a list
            of length capacity and each index is held as None at first

        Returns:
            This function returns nothing
        """
        self.items = [None]*capacity
        self.num_items = 0
        self.capacity = capacity

    def is_empty(self):
        """This function tells if the array has any not None items in it

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the array only contains None as it's elements.
            Otherwise it returns False.
        """
        return self.num_items == 0

    def is_full(self):
        """This function tells if the array has no spaces left to fill

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the array only contains any not None items as
            it's elements. Otherwise it returns False.
        """
        return (self.num_items) == self.capacity

    def push(self, item):
        """This functions adds a specified item to the top of the stack. If
            the stack is full an error is raised.

        Args:
            item - an item of any data type that will be added to the top
            of the stack

        Retruns:
            This function returns nothing
        """
        if self.is_full():
            raise IndexError("The stack is full")
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self):
        """This function takes the top item out of the stack. If the stack is
            empty an error is raised.

        Args:
            This function takes no arguments

        Returns:
            This function returns nothing
        """
        if self.is_empty():
            raise IndexError("The stack is empty")
        self.items[self.num_items-1] = None
        self.num_items -= 1

    def peek(self):
        """This function shows the top item of the stack. If the stack
            is empty an error is raised

        Args:
            This function takes no arguments

        Returns:
            This function returns the top item of the stack
        """
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.items[self.num_items - 1]

    def size(self):
        """This function returns the size of the stack

        Args:
            This function takes no arguments

        Returns:
            This function returns an integer that shows the size of the
            stack
        """
        return self.num_items

class StackLinked:
    """This class defines a stack that is built out of a linked list
    """
    def __init__(self, capacity):
        """This function initializes the stack

        Args:
            capacity(int) - this is an integer value that says how many
            items the list will be able to hold

            num_items(int) - this integer keeps track of how many nodes
            (that are not None) are in the list

            items(LinkedList) - this initializes a linked list with a
            head of none and a direction of none

        Returns:
            This function returns nothing
        """
        self.capacity = capacity
        self.items = LinkedList()
        self.num_items = 0

    def is_empty(self):
        """This function tells if the list has any not None items in it

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the list only contains None as it's elements.
            Otherwise it returns False.
        """
        return self.num_items == 0

    def is_full(self):
        """This function tells if the list has no spaces left to fill

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the list only contains any not None items as
            it's elements. Otherwise it returns False.
        """
        return self.num_items == self.capacity

    def push(self, item):
        """This functions adds a specified item to the top of the stack. If
            the stack is full an error is raised.

        Args:
            item - an item of any data type that will be added to the top
            of the stack

        Retruns:
            This function returns nothing
        """
        if self.is_full():
            raise IndexError("linked list is full")
        new_node = Node(item, None)
        new_node.next = self.items.head
        self.items.head = new_node
        self.num_items += 1

    def pop(self):
        """This function takes the top item out of the stack. If the stack is
            empty an error is raised.

        Args:
            This function takes no arguments

        Returns:
            This function returns nothing
        """
        if self.is_empty():
            raise IndexError("linked list is empty")
        old_node = self.items.head.next
        self.items.head = old_node
        self.num_items -= 1


    def peek(self):
        """This function shows the top item of the stack. If the stack
            is empty an error is raised

        Args:
            This function takes no arguments

        Returns:
            This function returns the top item of the stack
        """
        if self.is_empty():
            raise IndexError("linked list is empty")
        return self.items.head.first

    def size(self):
        """This function returns the size of the stack

        Args:
            This function takes no arguments

        Returns:
            This function returns an integer that shows the size of the
            stack
        """
        return self.num_items
