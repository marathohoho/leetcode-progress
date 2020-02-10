"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

def max_subarray(arr) :
	curr_max = global_max = arr[0]

	for i in range(1, len(arr)) :
		curr_max = max(curr_max + arr[i], arr[i])
		global_max = max(curr_max, global_max)

	return global_max


if __name__ == "__main__":
	print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
