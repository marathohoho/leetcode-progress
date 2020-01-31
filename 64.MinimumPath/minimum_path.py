"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from time import time

class Timed :
	def __init__(self, fn) :
		self.fn = fn

	def __call__(self, *args, **kwargs) :
		start = time()
		res = self.fn(*args, **kwargs)
		end = time()

		print(f'It took {end - start} seconds')
		return res

	''' Three different solutions '''
	'''
		O(m*n) time for all
		O(m*n) space for the first
		O(n) space for the second
		O(1) for the third solution
	'''

@Timed
def solution1(grid) :
	# solution 1
	if not grid :
		return 0

	# create a copy of the initial grid
	dp = [[row[i] for i in range(len(grid[0]))] for row in grid]

	# change the first row and first column of the dp matrix as
	# those will help us to compute the path
	# along the first row or column only

	for i in range(1, len(grid)) :
		dp[i][0] += dp[i-1][0]

	for j in range(1, len(dp[0])) :
		dp[0][j] += dp[0][j-1]

	for i in range(1, len(grid)) :
		for j in range(1, len(grid[0])) :
			dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

	return dp[-1][-1]

# soltuion with O(n) space
@Timed
def solution2(grid) :
	if not grid :
		return 0

	dp = [0] * len(grid[0])

	for i in range(len(grid)-1, -1, -1) :
		for j in range(len(grid[0])-1, -1, -1) :
			if i == len(grid) - 1 and j != len(grid[0]) - 1 :
				dp[j] = grid[i][j] + dp[j+1]
			elif i!= len(grid)-1 and j == len(grid[0]) - 1:
				dp[j] = grid[i][j] + dp[j]
			elif i != len(grid)-1 and j != len(grid[0]) -1 :
				dp[j] = grid[i][j] + min(dp[j], dp[j+1])
			else :
				dp[j] = grid[i][j]

	return dp[0]

@Timed
def solution3(grid) :
	if not grid :
		return 0

	for i in range(1, len(grid)) :
		grid[i][0] += grid[i-1][0]

	for j in range(1, len(grid[0])) :
		grid[0][j] += grid[0][j-1]

	for i in range(1, len(grid)) :
		for j in range(1, len(grid[0])) :
			grid[i][j] += min(grid[i-1][j], grid[i][j-1])
	return grid[-1][-1]
