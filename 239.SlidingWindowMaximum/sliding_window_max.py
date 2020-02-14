"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""


# O(n) time and O(k) space
from collections import deque
class MaxWindow :
	def __init__(self, arr, k) :
		self.arr = arr
		self.k = k
		self.index_q = deque()

	def solution(self) :
		if not self.arr or self.k == 1 : return self.arr

        # first iteration in range [0:k-1] to init our queue

		# keep track of the max index during the [0:k-1] iteration to append our first max element
        # into the result array

		max_number_index = 0
		result = []

		for i in range(self.k) :
			self.clean(i)
			self.index_q.append(i)

			max_number_index = i if self.arr[i] > self.arr[max_number_index] else max_number_index
		result.append(self.arr[max_number_index])

		# iterate the rest of the array to append the rest of the elements in arr
		for i in range(self.k, len(self.arr)) :
			self.clean(i)
			self.index_q.append(i)

			result.append(self.arr[self.index_q[0]])

		return result

	def clean(self, current_index) :
		# popleft the element outside our range k
        # k = 3, and index_q[0] = 1, current_index = 4, we need to popleft 4 - 3 == 1
		if self.index_q and self.index_q[0] == current_index - self.k : self.index_q.popleft()

		# pop out the values from the end of the que smaller than the value at the current_index
		while self.index_q and self.arr[self.index_q[-1]] < self.arr[current_index] : self.index_q.pop()

if __name__ == "__main__" :
	windows = MaxWindow([1,3,-1,-3,5,3,6,7,], k=3)
	print(windows.solution())


