import lru
import unittest

class Test(unittest.TestCase) :
	def testOne(self) :
		self.assertEqual(lru.solution())
