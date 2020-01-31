from DecodeWays import Solution
import unittest

class TestProgram(unittest.TestCase) :
	def test_one(self) :
		test = '12'
		self.assertEqual(Solution().decodeWays(test), 2)

	# def test_two(self) :
	# 	test = '345'
	# 	self.assertEqual(decodeWays(test), 1 )


if __name__ == '__main__' :
	unittest.main()
