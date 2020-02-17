"""
Given a non-empty array of integers, write a function that returns the longest strictly-increasing subsequence of the array.
A subsequence is defined as a set of numbers that are not necessarily adjacent but that are in the same order as they appear in the array.
Assume that there will only be one longest increasing subsequence.


Example : [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
Sample output: [-24, 2, 3, 5, 6, 35]

"""

"""
This is a dynamic programming problem with caching the lenghts of previous elements in array Lengths.
We also need to store all the preceeding elements indices in an array sequences

O(n*n) time and O(n) space
"""

def longestIncreasingSubsequence(arr) :
	lengths = [1 for num in arr]
	sequences = [None for num in arr]
	max_len_idx = 0

	for i in range(len(arr)) :
		curr_num = arr[i]
		for j in range(i) :
			other_num = arr[j]
			if other_num < curr_num and lengths[j] + 1 >= lengths[i] :
				lengths[i] = lengths[j] + 1
				sequences[i] = j
		if lengths[i] >= lengths[max_len_idx] :
			max_len_idx = i
	return buildSequence(arr, sequences, max_len_idx)

def buildSequence(arr, sequences, max_len_idx) :
	out = []
	while max_len_idx is not None :
		out.append(arr[max_len_idx])
		max_len_idx = sequences[max_len_idx]

	return list(reversed(out))


if __name__ == "__main__" :
	print(longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]))
