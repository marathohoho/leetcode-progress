"""Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.
For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".


Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""
"""
use a DP approach to solve this problem,
we will be holding a dictionary with words from words and the longest possible length so far.
"""

def solution(words) :
	# since we do not know if the words is sorted, we need
	# to sort in the increasing length order

	words.sort(key = lambda x : len(x))

	# need to store the longest length so far in the dictionary for every word in words

	dp = {word : 1 for word in words}

	for word in words :
		for i in range(len(word)) :
			temp = word[:i] + word[i+1:]
			if temp in dp :
				dp[word] = max(dp[word], dp[temp] + 1)


	print(dp)
	return max(dp.values())


if __name__ == "__main__" :
	print(solution(["a","b","ba","bca","bda","bdca"]))
