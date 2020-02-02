import unittest
import ReduceArray

class Test(unittest.TestCase) :
	def testOne(self) :
		self.assertEqual(ReduceArray.minSetSize([3,3,3,3,5,5,5,2,2,7]), 2)

	def testTwo(self) :
		self.assertEqual(ReduceArray.minSetSize([1,1,1,1,1]), 1)

	def testThree(self) :
		self.assertEqual(ReduceArray.minSetSize([1,2,3,4,5,6,7,8,9,10]), 5)

if __name__ == '__main__' :
	unittest.main()
