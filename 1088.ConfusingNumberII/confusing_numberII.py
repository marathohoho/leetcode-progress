"""We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.



Example 1:

Input: 20
Output: 6
Explanation:
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
Example 2:

Input: 100
Output: 19
Explanation:
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].


Note:

1 <= N <= 10^9"""


"""
Compose only the valid numbers.
Check if the number is the same as its rotation. Skip the case for leading 0, because it will cause the
repeated numbers.
Need to calculate the next possible rotation number.
Also, check that the number the next number to be added is less than N

"""

class Solution :
	def __init__(self) :
		self.mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
		self.valid_digits = [0,1,6,8,9]

	def confusingNumber2(self, N) :
		return self._dfs(0,0,1,N)

	def _dfs(self, num, rotation, digit, N) :
		res = 0
		if num != rotation : res += 1

		# add one more digit
		for d in self.valid_digits :
			# ignore the leading zero case
			if d == 0 and num == 0 :
				continue
			# check if the new nubmer is less than N
			if num * 10 + d <= N :
				res += self._dfs(num * 10 + d, self.mapping[d] * digit + rotation, 10 * digit, N)

		return res

