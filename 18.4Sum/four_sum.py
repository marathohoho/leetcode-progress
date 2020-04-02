'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution :
	def fourSum(self, nums, target) :
		final = []
		nums.sort() # sort the input to eliminate the duplicates O(N*LogN)
		left, right = 0, len(nums) - 1
		self.helper(nums, left, right, target, N, [], final)

	def helper(self, nums, left, right, target, N, current, final) :
		if N < 2 or right - left + 1 < N or nums[left] * N > target or nums[right] * N < target :
			return

		if N == 2 : # base case for adding the elements to the final array
			while left < right :
				sums = nums[left] + nums[right]
				if sums == target :
					final.append(current + [nums[left], nums[right]])
					left += 1
					while left < right and nums[left] == nums[left - 1] :
						left += 1
				elif sums < target :
					left += 1
				else :
					right -= 1

		else :
			# make recursive calls in case we still have elements N > 2 to add
			for i in range(left, right + 1) :
				if left == i or (i > left and nums[i] != nums[i-1]) :
					self.helper(nums, i+1, right, N-1, target - nums[i], current + [nums[i]], final)
