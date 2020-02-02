import k_weakest
import unittest

class Test(unittest.TestCase) :
	def testOne(self) :
		grid = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
		k = 3
		self.assertEqual(k_weakest.kWeakestRows(grid, k), [2,0,3])

	def testTwo(self) :
		grid = [[1,0,0,0], [1,1,1,1], [1,0,0,0],  [1,0,0,0]]
		k = 2
		self.assertEqual(k_weakest.kWeakestRows(grid, k), [0,2])


if __name__ == '__main__' :
	unittest.main()
