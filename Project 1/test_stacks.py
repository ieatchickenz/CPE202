from stacks import StackArray
from stacks import StackLinked
import unittest
from linked import LinkedList
from linked import Node


class TestCase(unittest.TestCase):
    def test_push(self):
        arr = StackArray(4)
        self.assertEqual(arr.is_empty(), True)
        self.assertEqual(arr.is_full(), False)
        arr.push(1)
        self.assertEqual(arr.peek(), 1)
        self.assertEqual(arr.size(), 1)
        arr.push(2)
        arr.push(3)
        arr.push(4)
        self.assertEqual(arr.is_full(), True)
        arr.pop()
        self.assertEqual(arr.peek(), 3)
        self.assertEqual(arr.size(), 3)
        
    def test_linked_list(self):
    	link = StackLinked(5)
    	self.assertEqual(link.is_empty(), True)
    	link.push(1)
    	self.assertEqual(link.peek(), 1)
    	self.assertEqual(link.size(), 1)
    	link.push(2)
    	link.push(3)
    	link.push(4)
    	link.push(5)
    	self.assertEqual(link.size(), 5)
    	self.assertEqual(link.is_full(), True)
    	link.pop()
    	self.assertEqual(link.peek(), 4)
    	self.assertEqual(link.size(), 4)

    def test_raises(self):
        link1 = StackLinked(2)
        arr1 = StackArray(2)
        node1 = Node(1, None)
        node2 = Node(2, node1)
        node3 = Node("too full", node2)
        self.assertRaises(IndexError,link1.pop)
        self.assertRaises(IndexError,arr1.pop)
        link1.push(node1)
        link1.push(node2)
        self.assertRaises(IndexError,link1.push, node3)
        arr1.push(1)
        arr1.push(2)
        self.assertRaises(IndexError, arr1.push, 3)




def main():
    # execute unit tests
    unittest.main()
if __name__ == '__main__':
    # execute main() function
    main()