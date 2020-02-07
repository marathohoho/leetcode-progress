"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

# almost the same approach as in 442.
# 1...n and n+1 elements. If we mark every referenced number in the array * (-1) and if we a number
# already marked as -1 then we know, someone else has marked it.

def find_dup(arr) :
	for i in range(len(arr)) :
		if arr[abs(arr[i])] < 0 :
			return abs(arr[i])
		arr[abs(arr[i])] *= -1


# since we cannot modify the array, we must solve it in a different way

def find_dup2(arr):
	# use hare tortoise method for finding a cycle detection and then
	# start from the 0th index and tortoise/hare position and start walking one step at a time

	tortoise = arr[0]
	hare = arr[arr[0]]

	# find intersection point
	while tortoise != hare :
		tortoise = arr[tortoise]
		hare = arr[arr[hare]]

	# find the entrance point to a cycle
	ptr1 = arr[0]
	ptr2 = arr[tortoise]

	while ptr1 != ptr2 :
		ptr1 = arr[ptr1]
		ptr2 = arr[ptr2]

	return ptr1

if __name__ == "__main__":
	print(find_dup2([1,2,2]))
	print(find_dup2([3,1,3,4,2]))
	print(find_dup2([1,3,4,2,2]))


