"""
Alex Petrov
CPE 202
Lab 3
"""
from linked import LinkedList
from linked import Node

class QueueArray:
    """This class defines a queue that is built out of an array
    """

    def __init__(self, capacity):
        """This function initializes the queue

        Args:
            capacity(int) - this is an integer value that says how many
            items the list will be able to hold

            num_items(int) - this integer keeps track of how many items
            (that are not None) are in the array

            items(list) - this is a list that is initialized as a list
            of length capacity and each index is held as None at first

            read_idx(int) - this integer keeps track of the last item
            in the queue for dequeueing

            write_idx(int) - this integer keeps track of the space one
            ahead of the first item fo enqueueing

        Returns:
            This function returns nothing
        """
        self.capacity = capacity
        self.items = [None]*(capacity+1)
        self.num_items = 0
        self.read_idx = 0
        self.write_idx = 0

    def is_empty(self):
        """This function tells if the array has any not None items in it

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the array only contains None as it's elements.
            Otherwise it returns False.
        """
        return self.read_idx == self.write_idx

    def is_full(self):
        """This function tells if the array has no spaces left to fill

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the array only contains any not None items as
            it's elements. Otherwise it returns False.
        """
        return self.read_idx == (self.write_idx + 1)%(len(self.items))

    def enqueue(self, item):
        """This functions adds a specified item to the end of the queue. If
            the queue is full an error is raised.

        Args:
            item - an item of any data type that will be added to the end of the queue

        Retruns:
            This function returns nothing
        """
        if self.is_full():
            raise IndexError("The queue is full")
        self.items[self.write_idx] = item
        self.write_idx += 1
        self.write_idx %= len(self.items)
        self.num_items += 1

    def dequeue(self):
        """This function takes the item at the front of the queue out. If the queue is
            empty an error is raised.

        Args:
            This function takes no arguments

        Returns:
            This function returns nothing
        """
        if self.is_empty():
            raise IndexError("The queue is empty")
        self.items[self.read_idx] = None
        self.read_idx += 1
        self.read_idx %= len(self.items)
        self.num_items -= 1

    def num_in_queue(self):
        """This function returns the size of the queue

        Args:
            This function takes no arguments

        Returns:
            This function returns an integer that shows the size of the
            queue
        """
        return self.num_items

class QueueLinked:
    """This class defines a queue that is built out of a linked list
    """
    def __init__(self, capacity):
        """This function initializes the stack

        Args:
            capacity(int) - this is an integer value that says how many
            items the list will be able to hold

            num_nodes(int) - this integer keeps track of how many nodes
            (that are not None) are in the list

            items(LinkedList) - this initializes a linked list with a
            head of none and a direction of none

        Returns:
            This function returns nothing
        """
        self.capacity = capacity
        self.items = LinkedList()
        self.num_nodes = 0

    def back_of_line(self):
        """This function keeps track of the node at front end of the queue

        Args:
            This function takes no arguments

        Returns:
            new_head - this function returns a node that is the node at the
            front of the queue
        """
        front = self.items.head
        while self.items.head.next.next is not None:
            self.items.head = self.items.head.next
        new_head = self.items.head
        self.items.head = front
        return new_head

    def is_empty(self):
        """This function tells if the list has any not None items in it

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the list only contains None as it's elements.
            Otherwise it returns False.
        """
        return self.num_nodes == 0

    def is_full(self):
        """This function tells if the list has no spaces left to fill

        Args:
            This function takes no arguments

        Returns:
            Boolean: True if the list only contains any not None items as
            it's elements. Otherwise it returns False.
        """
        return self.num_nodes == self.capacity

    def enqueue(self, item):
        """This functions adds a specified item to the back of the queue. If
            the queue is full an error is raised.

        Args:
            item - an item of any data type that will be added to the back
            of the queue

        Retruns:
            This function returns nothing
        """
        if self.is_full():
            raise IndexError("The queue is full")
        new_node = Node(item, None)
        new_node.next = self.items.head
        self.items.head = new_node
        self.num_nodes += 1

    def dequeue(self):
        """This function takes the item at the front of the queue out. If
            the queue is empty an error is raised.

        Args:
            This function takes no arguments

        Returns:
            This function returns nothing
        """
        if self.is_empty():
            raise IndexError("The queue is empty")
        back = self.back_of_line()
        back.next = None
        back.first = None
        self.num_nodes -= 1


    def num_in_queue(self):
        """This function returns the size of the queue

        Args:
            This function takes no arguments

        Returns:
            This function returns an integer that shows the size of the
            queue
        """
        return self.num_nodes
