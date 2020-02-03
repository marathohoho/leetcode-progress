import unittest
from critical_connections import test, test2, test3, test4

class Test(unittest.TestCase) :

	# def testOne(self) :
	# 	self.assertEqual(test.find_critical_connection(), [[1,3]])
	# def testTwo(self) :
	# 	self.assertEqual(test2.find_critical_connection(), [[1,4], [3,5], [0,1]])
	def testThree(self) :
		self.assertEqual(test3.find_critical_connection(), [])
	# def testFour(self) :
	# 	self.assertEqual(test4.find_critical_connection(), 12)

if __name__ == '__main__' :
	unittest.main()
