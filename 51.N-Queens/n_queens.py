"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

class Queens :
	def __init__(self, n) :
		self._n = n
		self._cols = [0] * n
		self._up = [0] * (2*n - 1)
		self._down = [0] * (2*n - 1)
		self._result = []
		self._queens = set()

	def solveQueens(self) :
		self._backtrack()
		return self._result

	def _backtrack(self, row = 0) :
		for col in range(self._n) :
			if self._can_place(row, col) :
				self._add_place(row, col)
				if row == self._n - 1 :
					self._add_solution()
				else :
					self._backtrack(row + 1)
				self._remove_place(row, col)

	def _can_place(self, row, col) :
		return not (self._cols[col] + self._up[row + col] + self._down[row - col])

	def _add_place(self, row, col) :
		self._queens.add((row, col))
		self._cols[col] = 1
		self._up[row + col] = 1
		self._down[row - col] = 1

	def _add_solution(self) :
		solution = []
		for _, col in sorted(self._queens) :
			solution.append('.' * col + 'Q' + '.' * (self._n - col - 1))
		self._result.append(solution)

	def _remove_place(self, row, col) :
		self._queens.remove((row, col))
		self._cols[col] = 0
		self._up[row + col] = 0
		self._down[row - col] = 0




def solveNQueens(n) :
	queens_solution = Queens(n)
	return queens_solution.solveQueens()


if __name__ == "__main__":
	print(solveNQueens(4))
