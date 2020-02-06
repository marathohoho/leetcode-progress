"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

def solution(arr) :
	res = []
	for i in range(1, len(arr) + 1) :
		arr[abs(arr[i-1]) - 1] = abs(arr[abs(arr[i-1]) - 1]) * (-1)

	for i in range(len(arr)) :
		if arr[i] > 0 :
			res.append(i+1)
	return res

if __name__ == "__main__":
	print(solution([4, 3, 2, 7, 8, 2, 3, 1]))
	print(solution([2, 1, 1, 5, 2, 6]))
