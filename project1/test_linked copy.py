'''
JeanReno Racines
CPE 202 - 07
PROJECT 1
1 - 13 - 19
'''


import unittest
from linked import *


class TestCase(unittest.TestCase):

    def test_Node_boilerplate(self):
        n1 = Node() # the head
        n2 = Node(2)
        n3 = Node(3)
        n1.point = n2
        n2.point = n3
        n11 = Node() # the head
        n22 = Node(2)
        n33 = Node(3)
        n11.point = n22
        n22.point = n33
        self.assertEqual(n1.__repr__(), "Elem: None   Point: -> (Elem: 2  " +
            " Point: -> (Elem: 3   Point: -> (None)))")
        self.assertEqual(n11.__repr__(), "Elem: None   Point: -> (Elem: 2  " +
            " Point: -> (Elem: 3   Point: -> (None)))")
        self.assertTrue(n1 == n11)
        n4 = Node(4)
        n44 = Node(4.1)
        n3.point = n4
        n33.point = n44
        self.assertEqual(n1.__repr__(), "Elem: None   Point: -> (Elem: 2  " +
            " Point: -> (Elem: 3   Point: -> (Elem: 4   Point: -> (None))))")
        self.assertEqual(n11.__repr__(), "Elem: None   Point: -> (Elem: 2  " +
            " Point: -> (Elem: 3   Point: -> (Elem: 4.1   Point: -> " +
            "(None))))")
        self.assertFalse(n1 == n11)
        n1.point = n3  #remove n2
        n11.point = n33  #remove n22
        self.assertEqual(n1.__repr__(), "Elem: None   Point: -> (Elem: 3  " +
            " Point: -> (Elem: 4   Point: -> (None)))")
        self.assertEqual(n11.__repr__(), "Elem: None   Point: -> (Elem: 3  " +
            " Point: -> (Elem: 4.1   Point: -> (None)))")
        self.assertFalse(n1 == n11)
        n5 = Node(1)
        n55 = Node ('1')
        n3.point = n5  #replace n4 with n5
        n33.point = n55  #replace n44 with n55
        self.assertEqual(n1.__repr__(), "Elem: None   Point: -> (Elem: 3  " +
            " Point: -> (Elem: 1   Point: -> (None)))")
        self.assertEqual(n11.__repr__(), "Elem: None   Point: -> (Elem: 3  " +
            " Point: -> (Elem: 1   Point: -> (None)))")
        self.assertFalse(n1 == n11)
        n6 = Node('1')  #replace n5 with n56
        n3.point = n6
        self.assertEqual(n1.__repr__(), "Elem: None   Point: -> (Elem: 3  " +
            " Point: -> (Elem: 1   Point: -> (None)))")
        self.assertEqual(n11.__repr__(), "Elem: None   Point: -> (Elem: 3  " +
            " Point: -> (Elem: 1   Point: -> (None)))")
        self.assertTrue(n1 == n11)        

    def test_Node_head(self):
        head = Node()
        self.assertEqual(head.elem, None)
        self.assertEqual(head.point, None)
        node_1 = Node(5)
        node_2 = Node('Jill')
        self.assertEqual(node_1.elem, 5)
        self.assertEqual(node_2.elem, 'Jill')

    def test_Node_point(self):
        head = Node()
        node_1 = Node(5)
        node_2 = Node('Jill')
        node_3 = Node(100)
        head.point = node_1
        node_1.point = node_2
        node_2.point = node_3
        self.assertEqual(head.elem, None)
        self.assertEqual(head.point.elem, 5)
        self.assertEqual(node_1.point.elem, 'Jill')
        self.assertEqual(node_2.point.elem, 100)

    def test_LinkedList_boilerplate(self):
        l1 = LinkedList()  # initialize the linked list
        l2 = LinkedList()
        l1.append(1)
        l1.append('alex')
        l1.append(2)
        l1.append('bang')
        l2.append(1)
        l2.append('alex')
        l2.append(2)
        l2.append('bang')
        self.assertEqual(l1.__repr__(), 'None, 1, alex, 2, bang')
        self.assertEqual(l2.__repr__(), 'None, 1, alex, 2, bang')
        self.assertTrue(l1 == l2)
        l1.remove(2)
        l2.remove(3)
        self.assertEqual(l1.__repr__(), 'None, 1, alex, bang')
        self.assertEqual(l2.__repr__(), 'None, 1, alex, 2')
        self.assertFalse(l1 == l2)
        l1.append_front('jojo')
        l2.append_front('ojoj')
        self.assertEqual(l1.__repr__(), 'None, jojo, 1, alex, bang')
        self.assertEqual(l2.__repr__(), 'None, ojoj, 1, alex, 2')
        self.assertFalse(l1 == l2)

    def test_LinkedList(self):
        lst = LinkedList()
        self.assertEqual(lst.length(), 0)
        self.assertRaises(IndexError, lst.get, 5)
        self.assertEqual(lst.head.elem, None)
        self.assertEqual(lst.head.point, None)
        lst.append(5)
        self.assertEqual(lst.length(), 1)
        self.assertEqual(lst.get(0), 5)
        self.assertRaises(IndexError, lst.get, 5)
        self.assertEqual(lst.head.elem, None)
        self.assertEqual(lst.head.point.elem, 5)
        lst.append_front('Jill')
        lst.append(101)
        lst.append('Bill')
        lst.remove(3)
        self.assertEqual(lst.length(), 3)
        self.assertEqual(lst.get(0), 'Jill')
        self.assertEqual(lst.get(2), 101)
        self.assertRaises(IndexError, lst.get, 5)
        self.assertEqual(lst.head.elem, None)
        self.assertEqual(lst.head.point.elem, 'Jill')


def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()
