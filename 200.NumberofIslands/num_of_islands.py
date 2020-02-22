"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

# The first method is to use UnionFind Data structure to group the islands. First,
# we will compute number of individual islands (not accounting for those islands being connected to each other),
# then we will connect the neighboring islands, and at each connection, we will decrease the counter.
# The final counter value will be the number of separate islands

class DSU :
	def __init__(self, grid) :
		rows, cols = len(grid), len(grid[0])
		self.par = [-1] * (rows * cols)
		self.rank = [0] * (rows * cols)
		self.counter = 0
		for i in range(rows) :
			for j in range(cols) :
				if grid[i][j] == 1 :
					self.par[i * cols + j] = i * cols + j
					self.counter += 1

	def find(self, x) :
		if self.par[x] != x :
			self.par[x] = self.find(self.par[x])
		return self.par[x]

	def union(self, x, y) :
		xp, yp = self.find(x), self.find(y)

		if xp != yp :
			if self.rank[xp] > self.rank[yp] :
				self.par[yp] = xp
			elif self.rank[xp] < self.rank[yp] :
				self.par[xp] = yp
			else :
				self.par[xp] = yp
			self.counter -= 1

class Solution :
	def _valid(self, grid, row, col) :
		rows, cols = len(grid), len(grid[0])
		return row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1

	def numIslands(self, grid) :
		if not grid or not grid[0] : return 0
		dsu = DSU(grid)
		rows, cols = len(grid), len(grid[0])

		# combine an island with neighboring islands
		neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
		for row in range(rows) :
			for col in range(cols) :
				if grid[row][col] == 1:
					for neighbor in neighbors :
						nr, nc = row + neighbor[0], col + neighbor[1]
						if self._valid(grid, nr, nc) :
							dsu.union(row * cols + col, nr * cols + nc)

		return dsu.counter

# the second solution is to DFS to explore all the neighbors
# first we traverse the matrix, and on the first accountance with an island,
# we count += 1 and dfs from that cell.
# Inside the dfs, we check the validity of the cell, and if it is equal to 1, we mark it as 0, and dfs from there

class Solution2 :
	def numIslands(self, grid) :
		if not grid or not grid[0] : return 0

		rows, cols = len(grid), len(grid[0])
		counter = 0
		for i in range(rows) :
			for j in range(cols) :
				if grid[i][j] == 1 :
					counter += 1
					self._dfs(grid, i, j)
		return counter

	def _dfs(self, grid, row, col) :
		rows, cols = len(grid), len(grid[0])
		if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1 :
			return
		grid[row][col] = 0
		self._dfs(grid, row+1, col)
		self._dfs(grid, row-1, col)
		self._dfs(grid, row, col+1)
		self._dfs(grid, row, col-1)

if __name__ == "__main__" :
	sol = Solution2()
	print(sol.numIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]))

