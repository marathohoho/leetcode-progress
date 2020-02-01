import unittest
import most_frequent_number

class Test(unittest.TestCase) :
	def testOne(self) :
		self.assertEqual(most_frequent_number.solution([1,1,2,5,6,5,5,9]), 5)


if __name__ == "__main__" :
	unittest.main()
