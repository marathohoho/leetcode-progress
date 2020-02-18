"""
Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively.
When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

Input: 89
Output: true
Explanation:
We get 68 after rotating 89, 86 is a valid number and 86!=89.

Input: 11
Output: false
Explanation:
We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.

"""

class Solution :
	def __init__(self) :
		self._rotations = { '0' : '0', '1': '1', '6' : '9', '8': '8', '9' : '6'}

	def confusingNumber(self, N) :
		stringed = str(N) :
		for char in stringed :
			if char not in self._rotations :
				return False

		return True if int(self.rotateNumber(list(stringed))) != N else False

	def rotateNumber(self, stringed_list) :
		out = ""
		for char in reversed(stringed_list) :
			out += char

		return out
