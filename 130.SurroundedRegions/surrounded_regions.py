"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

"""

Go over cells on the border, mark as 'Y' those that are 'O', dfs to their neighbors.
This way we will know which cells are on the border and connected to be
border cells.

Make the iteration over the whole board and remark all 'Y' -> 'O', and the rest 'O' -> 'X'

Time : O(rows * cols)
Space :  O(1)

"""

class SurroundedRegions :
	def solve(self, board) :
		if not board : return board

		self.ROWS, self. COLS = len(board), len(board[0])

		self.markBorders(board)

		for i in range(self.ROWS) :
			for j in range(self.COLS) :
				if board[i][j] == 'O' : board[i][j] = 'X'
				elif board[i][j] == 'Y' : board[i][j] = 'O'

	def markBorders(self, board) :
		for i in range(len(board)) :
			self.dfs(board, i, 0)
			self.dfs(board, i, self.COLS-1)
		for j in range(len(board[0])):
			self.dfs(board, 0, j)
			self.dfs(board, self.ROWS-1, j)

	def dfs(self, board, row, col) :
		if board[row][col] != 'O' : return
		board[row][col] = 'Y'
        if row < self.ROWS-1 : self.dfs(board, row+1, col)
        if row > 0 : self.dfs(board, row - 1, col)
        if col > 0 : self.dfs(board, row, col - 1)
        if col < self.COLS -1 : self.dfs(board, row, col + 1)
