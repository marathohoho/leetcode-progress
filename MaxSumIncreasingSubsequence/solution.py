def maxSumIncreasingSubsequence(arr) :
	sums = [num for num in arr]
	sequence = [None for x in arr]
	maxSumIndex = 0

	for i in range(len(arr)) :
		current_number = arr[i]
		for j in range(i) :
			number_before_current = arr[j]
			if current_number > number_before_current and current_number + sums[j] >= sums[i] :
				sums[i] = current_number + sums[j]
				sequence[i] = j
		if sums[i] >= sums[maxSumIndex] :
			maxSumIndex = i

	return [sums[maxSumIndex], construct_sequence(arr, sequence, maxSumIndex)]

def construct_sequence(arr, sequence, curr_index) :
	res = []
	while curr_index != None :
		res.append(arr[curr_index])
		curr_index = sequence[curr_index]

	return res[::-1]
