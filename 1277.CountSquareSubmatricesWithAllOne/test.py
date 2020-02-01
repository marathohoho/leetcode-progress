import unittest
import count_square

class Test(unittest.TestCase) :

	def testOne(self) :
		self.assertEqual(count_square.solution([[0,1,1,1], [1,1,1,1], [0,1,1,1]]), 15)

if __name__ == '__main__' :
	unittest.main()
