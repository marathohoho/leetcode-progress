import unittest
import minimum_path

class Test(unittest.TestCase) :
	def test_one(self):
		self.assertEqual(minimum_path.solution3([[1,3,1],[1,5,1],[4,2,1]]), 7)


if __name__ == '__main__' :
	unittest.main()
