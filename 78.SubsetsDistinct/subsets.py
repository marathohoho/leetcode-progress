"""
Given a set of distinct integers, arr, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: arr = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

def solution(arr) :
	def backtrack(level, length, current_set) :
		res.append(current_set[:])
		for i in range(level, length) :
			current_set.append(arr[i])
			backtrack(i + 1, length, current_set)
			current_set.pop()

	res = []
	backtrack(0, len(arr), [])
	return res


if __name__ == "__main__":
	print(solution([1,2,3]))
