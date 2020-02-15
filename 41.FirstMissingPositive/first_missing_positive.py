"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

def solution(arr) :
	n = len(arr)
	# if smallest possible positive number not in array, return it
	if 1 not in arr :
		return 1
	if n == 1 :
		return 2

	# since our number can lie only in the range [1, n+1] inclusive,
	# we do not need any values <1 and >n in our array
	for i in range(n) :
		if arr[i] < 1 or arr[i] > n :
			arr[i] = 1 # we can do this because by this time we already know that we do NOT have 1 in our array

	# mark the 'visited' numbers in array using
	# method of number as index method
	for i in range(n) :
		# eliminate the case that our target number is n (ans != n)
		if abs(arr[i]) == n :
			arr[0] = abs(arr[0]) * -1
		# apply (-1) visited markup to the number
		else :
			arr[abs(arr[i])] = abs(arr[abs(arr[i])]) * (-1)

	# print(arr)
	# now we need to conduct the check in order at which our result can appear
	# in range [1, n+1]
	# Since we already know that 1 is in our array, dont need to check it.

	# Check if number lies in range [2, n-1] inclusive.
	for i in range(1, n) :
		if arr[i] > 0:
			return i

	# check the number [n]
	if arr[0] > 0 :
		return n

	# if nothing worked, our number must be ans = n + 1
	return n + 1


if __name__ == "__main__":
	print(solution([3, 4, -1, 1]))
	print(solution([7,8,9,11,12]))
	print(solution([1,2,3]))
