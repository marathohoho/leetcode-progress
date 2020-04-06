'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

from collections import defaultdict

def solution(s) :
	res = defaultdict(list)

	for word in s :
		count = [0] * 26
		for c in word :
			count[ord(c) - ord('a')] += 1
		res[tuple(count)].append(word)

	return res.values()

# O(N * M) / O(N * M) time and space for N - number of words M - length of the longest word
