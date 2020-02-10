"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

def solution(arr, target) :
	def backtrack(current, start, end, target) :
		if target == 0 :
			res.append(current[:])

		elif target > 0 :
			for i in range(start, end) :
				current.append(arr[i])
				backtrack(current, i, end, target - arr[i])
				current.pop()

	res = []
	backtrack([], 0, len(arr), target)

	return res

if __name__ == "__main__":
	print(solution([2,3,5], 8))
