"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  """

  # the logic behind the solution for this problem is to
  # do bfs from each of the 0 "gates", on each bs neighbors level, keep track of the level of bfs.
  # This level will show the distance from the gate to a room.
  # To keep it always minimal, take the minimum between current distance and level + 1

from collections import deque
def solution(grid) :
	if not grid : return grid

	ROWS, COLS = len(grid), len(grid[0])

	# since we are using BFS we will need a queue ds.
	lvlq = deque()

	# we want to enque all the gates into the que
	# a queue entry will be a tuple with row, col, level triplet
	for i in range(ROWS) :
		for j in range(COLS) :
			if grid[i][j] == 0 :
				lvlq.append((i, j, 0))

	while lvlq :
		row, col, level = lvlq.popleft()

		# get the neighbors
		neighbors = [(0,1), (0,-1), (1,0), (-1,0)]

		for neighbor in neighbors :
			nr, nc = row + neighbor[0], col + neighbor[1]
			if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 2147483647 :
				continue
			grid[nr][nc] = level + 1
			lvlq.append((nr, nc, level+1))

	return grid


if __name__ == "__main__" :
	print(solution([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))
