def solution(arr) :
	for i in range(1, len(arr)) :
		for j in range(len(arr[0])) :
			if arr[i][j] == 1  :
				arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1

	return sum(map(sum, arr))
