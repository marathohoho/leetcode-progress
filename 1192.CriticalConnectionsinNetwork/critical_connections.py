"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

"""


# I will assume that we can have multiple disconnected components of the graph
# So we will run this algorithm on every node of the graph

# Otherwise, if we are said that the graph is on

from collections import defaultdict

class Solution :
	def __init__(self, connections, n) :
		self._n = n
		self.connections = connections
		self._graph =  defaultdict(list)
		self._id = 0
		self._low = [0] * n
		self._ids = [0] * n
		self._visited = [False] * n
		self._bridges = []

	def find_critical_connection(self) :
		# create a graph
		for from_, to_ in self.connections :
			self._graph[from_].append(to_)
			self._graph[to_].append(from_)

		for i in range(self._n) :
			if not self._visited[i] :
				self._dfs(i, -1)

		return self._bridges

	def _dfs(self, at, parent) :
		self._visited[at] = True
		self._id += 1

		# assign rank and id for the current node
		self._low[at] = self._ids[at] = self._id

		# traverse the child nodes
		for child in self._graph[at] :
			if child == parent : continue

			if not self._visited[child] :
				self._dfs(child, at)
				self._low[at] = min(self._low[at], self._low[child])

				# if cycle was not detected
				if self._ids[at] < self._low[child] :
					self._bridges.append([at, child])
			else :
				self._low[at] = min(self._low[at], self._ids[child])


test = Solution([[0,1],[1,2],[2,0],[1,3]], 4)
test2 = Solution([[0,1], [1,2], [1,3], [2,3], [3,5], [1,4]], 6)
test3 = Solution([[1,0],[2,0],[3,0],[4,1],[5,3],[6,1],[7,2],[8,1],[9,6],[9,3],[3,2],[4,2],[7,4],[6,2],[8,3],[4,0],[8,6],[6,5],[6,3],[7,5],[8,0],[8,5],[5,4],[2,1],[9,5],[9,7],[9,4],[4,3]], 10)
test4 = Solution([[0,1],[1,2],[2,0],[1,3]], 4)
