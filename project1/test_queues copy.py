'''
JeanReno Racines
CPE 202 - 07
PROJECT 1
1 - 13 - 19
'''


import unittest
from linked import *
from stacks import *
from queues import *


class TestCase(unittest.TestCase):

    def test_QueueArray_boilerplate(self):
        q1 = QueueArray(5) # initialize queue of capacity 5
        q2 = QueueArray(5)
        self.assertEqual(q1.__repr__(), "[None, None, None, None, None]")
        self.assertEqual(q2.__repr__(), "[None, None, None, None, None]")
        self.assertTrue(q1 == q2)
        q1.enqueue(5)
        q1.enqueue(6)
        q1.enqueue('Bob')
        q2.enqueue('Bob')        
        q2.enqueue(6)
        q2.enqueue(5)
        self.assertEqual(q1.__repr__(), "[Bob, 6, 5, None, None]")
        self.assertEqual(q2.__repr__(), "[5, 6, Bob, None, None]")
        self.assertTrue(q1 != q2)
        q1.enqueue(8)
        q1.enqueue('Joey')
        q2.enqueue(8)
        q2.enqueue('Joey')
        self.assertTrue(q1 != q2)
        self.assertEqual(q1.__repr__(), "[Joey, 8, Bob, 6, 5]")
        self.assertEqual(q2.__repr__(), "[Joey, 8, 5, 6, Bob]")
        q1.dequeue()
        q1.dequeue()
        q1.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        self.assertTrue(q1 == q2)
        self.assertEqual(q1.__repr__(), "[Joey, 8, None, None, None]")
        self.assertEqual(q2.__repr__(), "[Joey, 8, None, None, None]")
        q1.enqueue(1)
        q2.enqueue('1')
        self.assertFalse(q1 == q2)
        self.assertEqual(q1.__repr__(), "[1, Joey, 8, None, None]")
        self.assertEqual(q2.__repr__(), "[1, Joey, 8, None, None]")        

    def test_QueueArray(self):
        queue = QueueArray(5) # initialize queue of capacity 5
        self.assertEqual(queue.capacity, 5)
        self.assertEqual(queue.items, [None, None, None, None, None])
        self.assertEqual(queue.num_items, 0)
        self.assertEqual(queue.size(), 0)
        self.assertFalse(queue.is_full())
        self.assertTrue(queue.is_empty())
        self.assertRaises(IndexError, queue.dequeue)
        queue.enqueue(5)
        queue.enqueue(6)
        queue.enqueue('Bob')
        self.assertEqual(queue.capacity, 5)
        self.assertEqual(queue.items, ['Bob', 6, 5, None, None])
        self.assertEqual(queue.num_items, 3)
        self.assertEqual(queue.size(), 3)
        self.assertFalse(queue.is_full())
        self.assertFalse(queue.is_empty())
        queue.enqueue(8)
        queue.enqueue('Joey')
        self.assertEqual(queue.capacity, 5)
        self.assertEqual(queue.items, ['Joey', 8, 'Bob', 6, 5])
        self.assertEqual(queue.num_items, 5)
        self.assertEqual(queue.size(), 5)
        self.assertTrue(queue.is_full())
        self.assertFalse(queue.is_empty())
        self.assertRaises(IndexError, queue.enqueue, 4)
        queue.dequeue()
        self.assertEqual(queue.capacity, 5)
        self.assertEqual(queue.items, ['Joey', 8, 'Bob', 6, None])
        self.assertEqual(queue.num_items, 4)
        self.assertEqual(queue.size(), 4)
        self.assertFalse(queue.is_full())
        self.assertFalse(queue.is_empty())

    def test_QueueLinked_boilerplate(self):
        q1 = QueueLinked(5) # initialize queue of capacity 5
        q2 = QueueLinked(5)
        self.assertEqual(q1.__repr__(), "None")
        self.assertEqual(q2.__repr__(), "None")
        self.assertTrue(q1 == q2)
        q1.enqueue(5)
        q1.enqueue(6)
        q1.enqueue('Bob')
        q2.enqueue('Bob')        
        q2.enqueue(6)
        q2.enqueue(5)
        self.assertEqual(q1.__repr__(), "None, Bob, 6, 5")
        self.assertEqual(q2.__repr__(), "None, 5, 6, Bob")        
        self.assertTrue(q1 != q2)
        q1.enqueue(8)
        q1.enqueue('Joey')
        q2.enqueue(8)
        q2.enqueue('Joey')
        self.assertTrue(q1 != q2)
        self.assertEqual(q1.__repr__(), "None, Joey, 8, Bob, 6, 5")
        self.assertEqual(q2.__repr__(), "None, Joey, 8, 5, 6, Bob")
        q1.dequeue()
        q1.dequeue()
        q1.dequeue()
        q2.dequeue()
        q2.dequeue()
        q2.dequeue()
        self.assertTrue(q1 == q2)
        self.assertEqual(q1.__repr__(), "None, Joey, 8")
        self.assertEqual(q2.__repr__(), "None, Joey, 8")
        q1.enqueue(1)
        q2.enqueue('1')
        self.assertFalse(q1 == q2)
        self.assertEqual(q1.__repr__(), "None, 1, Joey, 8")
        self.assertEqual(q2.__repr__(), "None, 1, Joey, 8")

    def test_QueueLinked(self):
        queue = QueueLinked(5) # initialize queue of capacity 5
        self.assertEqual(queue.capacity, 5)
        # self.assertEqual(queue.items, [None, None, None, None, None])
        self.assertEqual(queue.num_items, 0)
        self.assertEqual(queue.num_in_queue(), 0)
        self.assertFalse(queue.is_full())
        self.assertTrue(queue.is_empty())
        self.assertRaises(IndexError, queue.dequeue)
        queue.enqueue(5)
        queue.enqueue(6)
        queue.enqueue('Bob')
        self.assertEqual(queue.capacity, 5)
        # self.assertEqual(queue.items, ['Bob', 6, 5, None, None])
        self.assertEqual(queue.num_items, 3)
        self.assertEqual(queue.num_in_queue(), 3)
        self.assertFalse(queue.is_full())
        self.assertFalse(queue.is_empty())
        queue.enqueue(8)
        queue.enqueue('Joey')
        self.assertEqual(queue.capacity, 5)
        # self.assertEqual(queue.items, ['Joey', 8, 'Bob', 6, 5])
        self.assertEqual(queue.num_items, 5)
        self.assertEqual(queue.num_in_queue(), 5)
        self.assertTrue(queue.is_full())
        self.assertFalse(queue.is_empty())
        self.assertRaises(IndexError, queue.enqueue, 4)
        queue.dequeue()
        self.assertEqual(queue.capacity, 5)
        # self.assertEqual(queue.items, ['Joey', 8, 'Bob', 6, None])
        self.assertEqual(queue.num_items, 4)
        self.assertEqual(queue.num_in_queue(), 4)
        self.assertFalse(queue.is_full())
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.capacity, 5)
        # self.assertEqual(queue.items, ['Joey', 8, None, None, None])
        self.assertEqual(queue.num_items, 2)
        self.assertEqual(queue.num_in_queue(), 2)
        self.assertFalse(queue.is_full())
        self.assertFalse(queue.is_empty())


def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()