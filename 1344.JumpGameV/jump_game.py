"""
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.


Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies.
"""

"""
The logic is to calculate the number of possible indices that we can visit starting from the smallest bar.
When we visit the larger bars, we already have precomputed values for the 'number of visitable indices' for the bar that we jumped on.

We need to iterate our array in increasing order of the heights of the bars

See more details in comments
"""

"""
O(n * d) time
O(n) space
"""
def solution(arr, d) :
	# need to sort the array by height of each element
	# we need to do this to get the order at which we need to visit each element
	# from smallest to tallest

	# make enumerated copy of the arr

	arr_enum = [0] * len(arr)
	for i, v in enumerate(arr) :
		arr_enum[i] = (i, v)

	# now sort the enumerated array by heights
	arr_enum = sorted(arr_enum, key = lambda x : x[1])

	# need index to visit array -> sequence of arrays to visit from the smallest to tallest bar
	index_to_visit = [pair[0] for pair in arr_enum]

	# now we have array of indices we need to visit in inreasing order of the height of the bars
	# we need visited_from array to keep the maximum number of indices we can visit if we start from that
	# index visited_from[index] holds max number if indices we can visit from 'index'

	visited_from = [0] * len(arr)
	# start travering the original array in order from the index_to_visit array
	for current_index in index_to_visit :
		# at each element we visit we need to check if we can jump left or right (up to d-times)
		# if it's reasonable to jump left or right
		# mark the index as visited
		visited_from[current_index] = 1
		for step_left in range(-1, -1*(d+1), -1) :
			if current_index + step_left  < 0 :
				break
			if arr[current_index] > arr[current_index + step_left] :
				visited_from[current_index] = max(visited_from[current_index], visited_from[current_index + step_left] + 1)
			else :
				break

		for step_right in range(1, d + 1) :
			if current_index + step_right  >= len(arr) :
				break
			if arr[current_index] > arr[current_index + step_right] :
				visited_from[current_index] = max(visited_from[current_index], visited_from[current_index + step_right] + 1)
			else :
				break

	print(max(visited_from))
	return max(visited_from)


