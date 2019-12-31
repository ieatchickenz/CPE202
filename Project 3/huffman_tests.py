import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist	= cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.key, 32)
      self.assertEqual(hufftree.min_val, 'a')
      left = hufftree.left
      self.assertEqual(left.key, 16)
      self.assertEqual(left.min_val, 'a')
      right = hufftree.right
      self.assertEqual(right.key, 16)
      self.assertEqual(right.min_val, 'd')

   def test_create_code(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')

   def test_01_encodefile(self):
      huffman_encode("file1.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))

   def test_01_decodefile(self):
      freqlist = cnt_freq("file1.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))

   def test_cnt_freq2(self):
      freqlist = cnt_freq("file2.txt")
      anslist = [0]*256
      anslist[32:117] = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 3, 1, 0, 2, 0,\
        2, 0, 1, 2, 0, 2, 2, 1, 0, 0, 3, 2]
      self.assertListEqual(freqlist[32:117], anslist[32:117])

   def test_create_huff_tree2(self):
      freqlist = cnt_freq("file2.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 35
      charforroot = "a"
      self.assertEqual(hufftree.key, 35)
      self.assertEqual(hufftree.min_val, ' ')
      left = hufftree.left
      self.assertEqual(left.key, 16)
      self.assertEqual(left.min_val, ' ')
      right = hufftree.right
      self.assertEqual(right.key, 19)
      self.assertEqual(right.min_val, 'a')

   def test_create_code2(self):
      freqlist = cnt_freq("file2.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('I')], '01000')
      self.assertEqual(codes[ord(' ')], '00')
      self.assertEqual(codes[ord('l')], '0110')

   def test_02_encodefile(self):
      huffman_encode("file2.txt", "output2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output2.txt", "output2_soln.txt"))

   def test_02_decodefile(self):
      freqlist = cnt_freq("file2.txt")
      huffman_decode(freqlist,"output2.txt", "decodefile2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile2.txt", "file2.txt"))

   def test_03_encodefile(self):
      huffman_encode("file4.txt", "output4.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output4.txt", "output4_soln.txt"))

   def test_03_decodefile(self):
      freqlist = cnt_freq("file4.txt")
      huffman_decode(freqlist,"output4.txt", "decodefile4.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      ans = open("decodefile4.txt", "r")
      lst = ans.readlines()
      ans.close()
      self.assertEqual(lst[0], "a 12")

   def test_04_nonefile(self):
      self.assertRaises(IOError, cnt_freq, 'lol.txt')
      with self.assertRaises(IOError):
         huffman_encode("fileeee.txt", "output1.txt")
      with self.assertRaises(IOError):
         freqlist = cnt_freq("file1.txt")
         huffman_decode(freqlist, "output1111.txt", "decodefile1.txt")

if __name__ == '__main__': 
   unittest.main()
