def solution(arr, target) :
	if not arr :
		return -1

	left, right = 0, len(arr) - 1

	while left < right :
		if arr[left] + arr[right] < target :
			left +=1
		elif arr[left] + arr[right] > target :
			right -= 1

		else :
			return [arr[left], arr[right]]

	return -1

if __name__ == "__main__" :
	print(solution([1,4,5,11], 15))

