"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.


Example 1 :
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.

Example 2 :
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.


"""

from collections import defaultdict
def minSetSize(arr) :
	if not arr :
		return 0
	length, half_length = len(arr), len(arr) // 2

	occurencies = defaultdict(int)

	for num in arr :
		occurencies[num] += 1

	sorted_occurencies = sorted(occurencies.values(), reverse = True)

	# greedely search number of occurencies that will satisfy the requieremt of  :
	# Return the minimum size of the set so that at least half of the integers of the array are removed.
	print(sorted_occurencies)
	size_of_set = 0
	for occurence_size in sorted_occurencies :
		length -= occurence_size
		size_of_set += 1
		if length <= half_length :
			return size_of_set
	return size_of_set
