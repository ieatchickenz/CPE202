"""
Alex Petrov
CPE 202
Lab 3
"""
from queues import QueueArray
from queues import QueueLinked
import unittest
from linked import LinkedList
from linked import Node

class TestCase(unittest.TestCase):
    def test_queue_arr(self):
        arr = QueueArray(5)
        self.assertEqual(arr.is_empty(), True)
        self.assertEqual(arr.is_full(), False)
        arr.enqueue(1)
        arr.enqueue(2)
        self.assertEqual(arr.num_in_queue(), 2)
        arr.enqueue(3)
        arr.enqueue(4)
        arr.enqueue(5)
        self.assertEqual(arr.num_in_queue(), 5)
        self.assertEqual(arr.is_full(), True)
        self.assertRaises(IndexError, arr.enqueue, "any")
        arr.dequeue()
        arr.dequeue()
        print(arr.items)
        self.assertEqual(arr.num_in_queue(), 3)
        arr.enqueue("four")
        self.assertEqual(arr.num_in_queue(), 4)
        arr.dequeue()
        arr.dequeue()
        arr.dequeue()
        arr.dequeue()
        self.assertRaises(IndexError, arr.dequeue)

    def test_queue_linked(self):
        link = QueueLinked(5)
        self.assertEqual(link.is_empty(), True)
        self.assertEqual(link.is_full(), False)
        link.enqueue(1)
        link.enqueue(2)
        self.assertEqual(link.num_in_queue(), 2)
        link.enqueue(3)
        link.enqueue(4)
        link.enqueue(5)
        self.assertEqual(link.num_in_queue(), 5)
        self.assertEqual(link.is_full(), True)
        self.assertRaises(IndexError, link.enqueue, "any")
        link.dequeue()
        link.dequeue()
        self.assertEqual(link.num_in_queue(), 3)
        link.enqueue("four")
        self.assertEqual(link.num_in_queue(), 4)
        link.dequeue()
        link.dequeue()
        link.dequeue()
        link.dequeue()
        self.assertRaises(IndexError, link.dequeue)
def main():
    unittest.main()

if __name__ == '__main__':
    main()