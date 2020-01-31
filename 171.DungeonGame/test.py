import unittest
import dungeon

class Test(unittest.TestCase) :
	def test_one(self) :
		self.assertEqual(dungeon.solution([[-2,-3,3],[-5,-10,1],[10,30,-5]]), 7)

if __name__ == "__main__" :
	unittest.main()
