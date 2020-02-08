"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Accepted
"""

def next_largest_index(nums: list, i:  int) :
	j = len(nums) - 1

	while nums[j] <= nums[i] :
		j -= 1

	return j

def solution(nums:list):
	if not nums or len(nums) == 1 :
		return []

	tipping_point = -1

	for i in range(len(nums)-1, -1, -1) :
		if nums[i] > nums[i-1] :
			tipping_point = i - 1 # this is the index of the number which will be swapped
			break

	if tipping_point == -1 :
		# we have the largest possible combination, return the reverse of it to get the smallest combination
		nums.reverse()
		return nums

	# next step is to swap the tipping point with the next larges number in nums[i:]
	# since we know that all of the numbers in nums[i+1: ] are in increasing order from the end, we should look from the end

	next_largest_value_index = next_largest_index(nums, tipping_point)

	# swap those two numbers
	nums[tipping_point], nums[next_largest_value_index] = nums[next_largest_value_index], nums[tipping_point]
	nums[tipping_point + 1 : ] = nums[tipping_point + 1 : ][::-1]

	return nums

if __name__ == "__main__":
	print(solution([1,2,3]))
	print(solution([1,2,7,4,8,5,3]))
	print(solution([3,2,1]))
	print(solution([1,1,5]))

