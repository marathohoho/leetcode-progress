import longest_common_subsequence
import unittest

class Test(unittest.TestCase) :
	# def testOne(self) :
	# 	self.assertEqual(longest_common_subsequence.solution("zxvvyzw", "xkykzpw"), "xyzw")
	# def testTwo(self) :
	# 	self.assertEqual(longest_common_subsequence.solution("xkykzpw", "zxvvyzw"), "xyzw")
	def testThree(self) :
		self.assertEqual(longest_common_subsequence.solution("abkzpc", "bz25c9"), "bzc")


if __name__ == '__main__' :
	unittest.main()
