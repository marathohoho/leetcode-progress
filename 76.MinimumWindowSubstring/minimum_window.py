"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

"""
The idea behind the solution is to use a sliding window between left and right pointers on the string S.
In order to keep track of number of occurencies of a letter inside a string, we use a defaultdict(int).
Initialize default dict for both S and T.
we also need a counter that will show the number of charachters that have been formed in S's window matching T

Increase right while we don't get window containig all characters from T

then, we need to decrease the size of the window (left+=1) each time checking if the letter from T disappeared from the window.

keep the length, left, right inside a tuple
"""
from collections import defaultdict
def solution(S, T) :
	if not S or not T : return ""

	dict_t = defaultdict(int)
	for char in T :
		dict_t[char] += 1

	window = defaultdict(int)
	l, r = 0, 0

	ans = (float('inf'), None, None)

	# number of unique characters from T
	required = len(dict_t)

	# number of unique characters formed from S window
	formed = 0
	while r < len(S) :
		c = S[r]
		window[c] += 1
		if c in dict_t and window[c] == dict_t[c] : formed += 1

		while l <=  r and formed == required :
			c = S[l]
			if r - l + 1 < ans[0] : ans = (r-l+1, l, r)
			window[c] -= 1
			if c in dict_t and window[c] < dict_t[c] : formed -= 1
			l += 1
		r += 1


	return "" if ans[0] == float('inf') else S[ans[1] : ans[2] + 1]


if __name__ == "__main__" :
	print(solution('ADOBECODEBANC', 'ABC'))

