"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


def find_all_duplicates(arr) :
	# since the numbers in array are limited to 1 ... n
	# then we can use the number as a reference (index) to the next number of arr

	res = []

	for i in range(1, len(arr)) :
		if arr[abs(arr[i-1])-1] < 1 :
			res.append(abs(arr[i-1]))
		else :
			arr[abs(arr[i-1])-1] *= -1
	return res

if __name__ == "__main__":
	print(find_all_duplicates([4,3,2,7,8,2,3,1]))
