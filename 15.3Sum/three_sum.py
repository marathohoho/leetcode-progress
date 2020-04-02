'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


# O(N*logN + N^2) for time and O(1) for space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
		final = []
		nums.sort()

		for i in range(len(nums) - 2):
			if nums[i] > 0 : break # if the current number is larger than 0, the next number will be same or equal
			if i > 0 and nums[i] == nums[i-1] : continue # skip the duplicate numbers

			left, right = i + 1, len(nums)-1

			while left < right :
				sums = nums[i] + nums[left] + nums[right]
				if sums < 0 :
					left += 1
				elif sums >0 :
					right -= 1

				else :
					final.append([nums[i], nums[left], nums[right]])
					while left < right and nums[left] == nums[left + 1] :
						left += 1
					while left < right and nums[right] == nums[right - 1] :
						right -= 1

					left += 1
					right -= 1
		return final

