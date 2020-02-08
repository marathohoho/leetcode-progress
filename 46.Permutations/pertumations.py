class Solution :
	def __init__(self) :
		self.result = []

	def permutations(self, nums) :
		if not nums or len(nums) == 1 :
			return nums

		self.backtrack(0, nums)
		return self.result

	def backtrack(self, level, nums) :
		if level == len(nums) :
			self.result.append(nums[:])

		for i in range(level, len(nums)) :
			nums[level], nums[i] = nums[i], nums[level]
			self.backtrack(level + 1, nums)
			nums[level], nums[i] = nums[i], nums[level]

		return

if __name__ == "__main__":
	solution = Solution()
	print(solution.permutations([1,2,3]))
