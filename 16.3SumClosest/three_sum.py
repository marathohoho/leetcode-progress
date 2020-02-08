"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

def three_sum(arr, target) :
	arr.sort()
	res = dict()

	for i in range(len(arr) - 2 ) :
		if i != 0 and arr[i] == arr[i-1] :
			continue

		left = i + 1
		right = len(arr) - 1
		while left < right :
			total = arr[left] + arr[i] + arr[right]
			diff = abs(total - target)
			res[diff] = total
			if total < target :
				print(left, right)
				left += 1
			elif total > target :
				print(left, right)
				right -= 1

			else :
				return total

		return res[min(res)]

if __name__ == "__main__":
	print(three_sum(
[-1,2,1,-4],
1))
