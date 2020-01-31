from unique_paths import uniqueWays
import unittest
from unittest import TestCase

class Test(TestCase) :
	def test_one(self) :
		self.assertEqual(uniqueWays(3,2), 3)

	def test_two(self) :
		self.assertEqual(uniqueWays(7, 3), 28)

if __name__ == "__main__" :
	unittest.main()
