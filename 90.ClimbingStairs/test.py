import unittest
from climbing_stairs import solution
class Test(unittest.TestCase) :
	def test_one(self) :
		self.assertEqual(solution(4), 5)
	def test_two(self) :
		self.assertEqual(solution(3), 3)
	def test_three(self) :
		self.assertEqual(solution(5), 8)

if __name__ == '__main__' :
	unittest.main()
