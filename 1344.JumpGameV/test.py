import jump_game
import unittest

class Test(unittest.TestCase) :
	def testOne(self) :
		self.assertEqual(jump_game.solution([6,4,14,6,8,13,9,7,10,6,12], d = 2), 4)
if __name__ == '__main__' :
	unittest.main()
