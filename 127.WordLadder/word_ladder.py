"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

# this is a graph problem, we will use BFS traveral with level count.
# need to contruct a graph of word combinations with one letter removed
# need to keep track of the "visited" words

from collections import defaultdict, deque
def solution(begin_word, end_word, word_list) :
	if not word_list or not end_word or not begin_word or end_word not in word_list : return -1

	candidates = defaultdict(list)
	length = len(begin_word)

	visited = set()
	visited.add(begin_word)

	wordsq = deque([(begin_word, 1)])
	# O(length * words_list)
	for word in word_list :
		for i in range(length) :
			candidates[word[:i] + '*' + word[i+1:]].append(word)
	while wordsq :
		word, level = wordsq.popleft()
		for i in range(length) :
			intermediate_word = word[:i] + '*' + word[i+1:]
			for candidate in candidates[intermediate_word] :
				if candidate == end_word :
					return level + 1
				if candidate not in visited :
					visited.add(candidate)
					wordsq.append((candidate, level + 1))
	print(wordsq)
	return -1

if __name__ == "__main__" :
	print(solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
