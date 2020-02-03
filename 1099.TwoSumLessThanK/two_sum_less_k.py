# must be l < r
# A[l] + A[r] = S; S < K
# A[l] + A[r] < K
# -> therefore, must me A[l] < K - A[r]

# O(nlogn) time / constant space
def solution(arr, k) :
	arr.sort()
	l, r = 0, len(arr) - 1
	max_sum = float('-inf')
	while l < r :
		if arr[l] < k - arr[r] :
			max_sum = max(max_sum, arr[l] + arr[r])
			l += 1
		else :
			r -= 1

	return -1 if max_sum == float('-inf') else max_sum


if __name__ == "__main__" :
	print(solution([23,24, 1, 8, 33, 34, 75, 54], 60))
