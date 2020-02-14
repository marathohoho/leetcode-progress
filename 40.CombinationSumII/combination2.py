"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
def solution(arr, target) :
	def backtrack(curr, start, end, target) :
		if target == 0 :
			res.append(curr[:])

		elif target > 0 :
			for i in range(start, end) :
				if i != start and arr[i] == arr[i-1] :
					continue
				curr.append(arr[i])
				backtrack(curr, i + 1, end, target - arr[i])
				curr.pop()

	res = []
	arr.sort()
	backtrack([], 0, len(arr), target)
	return res


if __name__ == "__main__":
	print(solution([2,5,2,1,2], 5))
