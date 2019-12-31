from stacks import StackArray
from exp_eval import *
import unittest

class TestCase(unittest.TestCase):
	def test_postfix1(self):
		a = "( ( 5 - 3 ) ^ 2 + ( 4 - 2 ) ^ 2 ) ^ ( 1 / 2 )"
		b = "( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )"
		c = "10 + 3 * 5 / ( 16 - 4 )"
		d = "5 * 3 ^ ( 4 - 2 )"
		e = "( ( 1 * 2 ) + ( 3 / 4 ) )"
		f = "( ( 2 * ( 3 + 4 ) ) / 5 )"
		g = "( 3 * ( 4 + 6 / 3 ) )"
		h = "~ 3 * 3 + 9"
		i = "( ~ 3 ) ^ 2 + 9"
		j = "~ 3 ^ 2 + 9"
		k = "4 ^ ( ~ 1 ) * 4"
		l = "1"
		self.assertEqual(infix_to_postfix(a), "5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^")
		self.assertEqual(infix_to_postfix(b), "15 7 1 1 + - / 3 * 2 1 1 + + -")
		self.assertEqual(infix_to_postfix(c), "10 3 5 * 16 4 - / +")
		self.assertEqual(infix_to_postfix(d), "5 3 4 2 - ^ *")
		self.assertEqual(infix_to_postfix(e), "1 2 * 3 4 / +")
		self.assertEqual(infix_to_postfix(f), "2 3 4 + * 5 /")
		self.assertEqual(infix_to_postfix(g), "3 4 6 3 / + *")
		self.assertEqual(infix_to_postfix(h), "3 ~ 3 * 9 +")
		self.assertEqual(infix_to_postfix(i), "3 ~ 2 ^ 9 +")
		self.assertEqual(infix_to_postfix(j), "3 2 ^ ~ 9 +")
		self.assertEqual(infix_to_postfix(k), "4 1 ~ ^ 4 *")
		self.assertEqual(infix_to_postfix(l), "1")

		self.assertEqual(postfix_eval(infix_to_postfix(a)), 2.8284271247461903)
		self.assertEqual(postfix_eval(infix_to_postfix(b)), 5.0)
		self.assertEqual(postfix_eval(infix_to_postfix(c)), 11.25)
		self.assertEqual(postfix_eval(infix_to_postfix(d)), 45)
		self.assertEqual(postfix_eval(infix_to_postfix(e)), 2.75)
		self.assertEqual(postfix_eval(infix_to_postfix(f)), 2.8)
		self.assertEqual(postfix_eval(infix_to_postfix(g)), 18.0)
		self.assertEqual(postfix_eval(infix_to_postfix(h)), 0)
		self.assertEqual(postfix_eval(infix_to_postfix(i)), 18)
		self.assertEqual(postfix_eval(infix_to_postfix(j)), 0)
		self.assertEqual(postfix_eval(infix_to_postfix(k)), 1.0)
		self.assertEqual(postfix_eval(infix_to_postfix(l)), 1)

	def test_valid(self):
		infix = " ( 1 + 2 ) * 15 - 4 ^ ( 2 )"
		self.assertTrue(infix_valid(infix))
		infix = ""
		self.assertRaises(SyntaxError, infix_valid, infix)
		infix = " ( 1 + 2 ) * 15 - 4 ^ ( 2 ) )"
		self.assertRaises(SyntaxError, infix_valid, infix)
		infix = infix = " ( 1 + 2 ) * 15 - 4 ^ ( 2  3 ) "
		self.assertRaises(SyntaxError, infix_valid, infix)

		postfix = "5 3 4 2 - ^ *"
		self.assertTrue(postfix_valid(postfix))
		postfix = "3 4 4 6 3 / + *"
		self.assertFalse(postfix_valid(postfix))
		postfix = "4 1 ~ ^ 4 * ^"
		self.assertFalse(postfix_valid(postfix))
		postfix = "1"
		self.assertTrue(postfix_valid(postfix))
		postfix = "1 ~ ~ ~ ~ "
		self.assertTrue(postfix_valid(postfix))

	def test_zero_div(self):
		postfix = "1 2 + 0 /"
		self.assertRaises(ZeroDivisionError, postfix_eval, postfix)



def main():
    # execute unit tests
    unittest.main()
if __name__ == '__main__':
    # execute main() function
    main()
 