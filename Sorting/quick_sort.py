"""
Given a list of integer numbers arr, sort the arr using a quick sort.
Provide time and space complexities.
"""

def quickSort(arr) :
	quickSortHelper(arr, 0, len(arr) - 1)
	return arr

def quickSortHelper(arr, start, end) :
	if start >= end :
		return
	pivot = start
	left = pivot + 1
	right = end
	while left <= right :
		if arr[left] > arr[pivot] and arr[right] < arr[pivot] :
			arr[left], arr[right] = arr[right], arr[left]
		if arr[left] <= arr[pivot] :
			left += 1
		if arr[right] >= arr[pivot] :
			right -= 1
	# swap pivot and the right
	arr[pivot], arr[right] = arr[right], arr[pivot]

	right_subarray_is_larger = end - (right + 1) > (right - 1) - start
	if right_subarray_is_larger :
		quickSortHelper(arr, start, right - 1)
		quickSortHelper(arr, right + 1, end)
	else :
		quickSortHelper(arr, right + 1, end)
		quickSortHelper(arr, start, right - 1)
	return

if __name__ == "__main__" :
	print(quickSort([12,-4,4,100,23]))
