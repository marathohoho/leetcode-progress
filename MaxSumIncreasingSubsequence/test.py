import unittest
import solution

class Test(unittest.TestCase) :
	def test_one(self)  :
		self.assertEqual(solution.maxSumIncreasingSubsequence([5,4,3,2,1]), [5, [5]])
	def test_two(self)  :
		self.assertEqual(solution.maxSumIncreasingSubsequence([1,2,3,4,5]), [15, [1,2,3,4,5]])
	def test_three(self)  :
		self.assertEqual(solution.maxSumIncreasingSubsequence([10,70,20,30,50,11,30]), [110,[10,20,30,50]])

if __name__ == '__main__'  :
	unittest.main()
