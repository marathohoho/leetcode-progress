"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]"""

def solution(arr) :
	def backtrack(level, length, current_set) :
		res.append(current_set[:])
		for i in range(level, length) :
			if i != level and arr[i] == arr[i-1] : continue

			current_set.append(arr[i])
			backtrack(i + 1, length, current_set)
			current_set.pop()

	res = []
	arr.sort()
	backtrack(0, len(arr), [])

	return res


if __name__ == "__main__":
	print(solution([1,2,2]))
