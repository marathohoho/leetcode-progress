import unittest
import knapsack

class Test(unittest.TestCase) :
	def testOne(self) :
		self.assertEqual(knapsack.solution([[1,2], [4,3], [5,6], [6,7]], 10), [10, [1, 3]])

if __name__ == "__main__" :
	unittest.main()
