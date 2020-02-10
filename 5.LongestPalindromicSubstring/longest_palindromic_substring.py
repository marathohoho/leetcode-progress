"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def expand(s, l ,r) :
	while l >= 0 and r < len(s) and s[l] == s[r] :
		l -= 1
		r += 1
	# we do not want to include the ends that are not equal
	return s[l+1:r]

def longest_palidrome(s) :
	# use method of expanding around the center
	# we have 2*n - 1 such centers around which there can be a palidrome
	if not s :
		return s

	longest_so_far = s[0:1]

	# we want to traverse the string and find all the centers of the palindrome
	for i in range(len(s)) :
		# for the palindrome with a letter as a center
		temp = expand(s, i, i)
		if len(temp) > len(longest_so_far) :
			longest_so_far = temp

		temp = expand(s, i, i+1)
		if len(temp) > len(longest_so_far) :
			longest_so_far = temp

	return longest_so_far


if __name__ == "__main__":
	print(longest_palidrome('babad'))
