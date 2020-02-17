"""
You are given two non-empty strings.
The first one is a pattern consisting of only "x"s and / or "y"s; the other one is a normal string of alphanumeric characters.
Write a function that checks whether or not the normal string matches the pattern.
A string S0 is said to match a pattern if replacing all "x"s in the pattern with some string S1 and replacing all "y"s in the pattern with some string S2 yields the same string S0.
If the input string does not match the input pattern, return an empty array; otherwise, return an array holding the representations of "x" and "y" in the normal string, in that order.
If the pattern does not contain any "x"s or "y"s, the respective letter should be represented by an empty string in the final array that you return.
Assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and "y" in the input string.

Example:
sample input : s1 = "xxyxxy", s2 = "gogogpowerrangergogopowerranger"

"""
from collections import defaultdict


def patternMatcher(pattern, string) :
	if len(pattern) > len(string) :
		return []

	# get new pattern if we have to swap x and y letters
	# take a mark if we did swap or not
	new_pattern = getNewPattern(pattern)
	did_swap = new_pattern[0] != pattern[0]

	# hold number of occurencies for each character of the pattern
	occurencies = defaultdict(int)

	first_y_pos = getCountsAndFirstYPos(new_pattern, occurencies)

	if occurencies['y'] != 0 :
		# if we have ys in our pattern
		string_length = len(string)
		for len_of_x in range(1, string_length) :
			len_of_y = (string_length - len_of_x * occurencies['x']) / occurencies['y']
			if len_of_y % 1 or len_of_y <= 0 :
				continue
			len_of_y = int(len_of_y)
			y_index = first_y_pos * len_of_x
			x = string[:len_of_x]	# g
			y = string[y_index : y_index + len_of_y] #gopowerranger

			potential_match = map(lambda char : x if char == 'x' else y, new_pattern)
			if string == "".join(potential_match) :
				return [x, y] if not did_swap else [y, x]

	else :
		len_of_x = len(string) / occurencies['x']
		if len_of_x % 1 != 0 :
			len_of_x = int(len_of_x)
			x = string[:len_of_x]
			potential_match = map(lambda char : x, new_pattern)
			if string == "".join(potential_match) :
				return [x, ""] if not did_swap else ["", x]



def getNewPattern(pattern) :
	patterLetters = list(pattern)
	if pattern[0] == 'x' :
		return patterLetters
	else :
		return list(map(lambda char : 'x' if char == 'y' else 'y', patterLetters))

def getCountsAndFirstYPos(pattern, occurencies):
	first_occurence = -1

	for i, letter in enumerate(pattern) :
		occurencies[letter] += 1
		if letter == 'y' and first_occurence == -1 :
			first_occurence = i

	return first_occurence

if __name__ == "__main__" :
	print(patternMatcher('xxyxxy', 'gogopowerrangergogopowerranger'))
