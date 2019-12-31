import unittest
from my_graph import *
from queues import *
from linked import *

class TestCase(unittest.TestCase):
    def test_one(self):
        g = Graph("testinput1.txt")
        dsf = g.get_conn_components()
        g1 = Graph("testinput1.txt")
        bsf = g1.get_conn_components_bfs()
        self.assertEqual(dsf, [[1, 2, 3, 4, 5], [6, 7, 9, 8]])
        self.assertEqual(bsf, [[1, 2, 3, 4, 5], [6, 7, 8, 9]])
        self.assertTrue(g.is_bicolor)

    def test_two(self):
        g = Graph("testinput2.txt")
        dsf1 = g.get_conn_components()
        # print(dsf)
        g1 = Graph("testinput2.txt")
        bsf1 = g1.get_conn_components_bfs()
        self.assertEqual(dsf1, [[1, 2, 3], [4, 6, 7, 8], [5]])
        self.assertEqual(bsf1, [[1, 2, 3], [4, 6, 7, 8], [5]])
        self.assertFalse(g.is_bicolor)

    def test_three(self):
        g = Graph("testinput3.txt")
        dsf1 = g.get_conn_components()
        # print(dsf)
        g1 = Graph("testinput3.txt")
        bsf1 = g1.get_conn_components_bfs()
        self.assertEqual(dsf1, [[1, 2, 3, 4, 5, 6, 8], [7, 9, 10]])
        self.assertEqual(bsf1, [[1, 2, 3, 4, 5, 6, 8], [7, 9, 10]])
        self.assertFalse(g.is_bicolor)

    def test_four(self):
        g = Graph("testinput4.txt")
        dsf1 = g.get_conn_components()
        # print(dsf)
        g1 = Graph("testinput4.txt")
        bsf1 = g1.get_conn_components_bfs()
        self.assertEqual(dsf1, [[1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94,\
         7, 93, 8, 92, 9, 91, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,\
          22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38,\
           39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55,\
            56, 57, 58, 59], [60, 70, 80], [61], [62], [63], [64], [65], [66], [67],\
             [68], [69], [71], [72], [73], [74], [75], [76], [77], [78], [79], [81],\
              [82], [83], [84], [85], [86], [87], [88], [89], [90], [100]])
        self.assertEqual(bsf1, [[1, 99, 10, 91, 9, 92, 8, 93, 7, 94, 6, 95,\
         5, 11, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [2, 98, 3, 97, 4, 96],\
          [12, 13, 14, 15, 16, 17, 18, 19, 20], [31, 32, 33, 34, 35, 36, 37, 38,\
           39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55,\
            56, 57, 58, 59], [60, 70, 80], [61], [62], [63], [64], [65], [66], [67],\
             [68], [69], [71], [72], [73], [74], [75], [76], [77], [78], [79], [81],\
              [82], [83], [84], [85], [86], [87], [88], [89], [90], [100]])
        self.assertFalse(g.is_bicolor)

def main():
    unittest.main()
if __name__ == '__main__':
    main()