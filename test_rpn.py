import unittest
import rpn

class TestBasics (unittest.TestCase):
	def test_add (self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2,result)
	def test_adds (self):
		result = rpn.calculate("1 1 + 2 +")
		self.assertEqual(4,result)
	def test_subtract(self):
		result = rpn.calculate("5 2 -")
		self.assertEqual(3,result)
	def test_multiply(self):
		result = rpn.calculate("5 2 *")
		self.assertEqual(10,result)
	def test_divide(self):
		result = rpn.calculate("5 2 /")
		self.assertEqual(2.5,result)
	def test_percentage(self):
		result = rpn.calculate("5 2 %")
		self.assertEqual(40,result)
	def test_exponent(self):
		result = rpn.calculate("2 3 ^")
		self.assertEqual(8,result)
	def test_intdiv(self):
		result = rpn.calculate("5 2 .")
		self.assertEqual(2,result)
	def test_toomany(self):
		with self.assertRaises(TypeError):
			result = rpn.calculate("1 2 3 +")
