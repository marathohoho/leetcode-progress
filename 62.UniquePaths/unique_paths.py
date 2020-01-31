'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''

from time import time
class Timed:
	def __init__(self, fn) :
		self.fn = fn

	def __call__(self, *args, **kwargs) :
		start = time()
		res = self.fn(*args, **kwargs)
		end = time()

		print(f'Execution took {end - start} seconds')
		return res

@Timed
def uniqueWays(m, n) :
	dp = [[1 for j in range(n)] for i in range(m)]

	for i in range(1, m):
		for j in range(1, n) :
			dp[i][j] = dp[i][j-1] + dp[i-1][j]
	return dp[-1][-1]
