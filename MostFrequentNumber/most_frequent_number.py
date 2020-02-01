"""
Given array of numbers, output the most frequent number.

Example [1,1,2,5,6,5,5,5,5,5,9] -> 5
"""

from collections import defaultdict
from time import time

class Timed :
	def __init__(self, fn) :
		self.fn = fn
	def __call__(self, *args, **kwargs) :
		start = time()
		res = self.fn(*args, **kwargs)
		end = time()

		print(f'Execution took {end - start} seconds')
		return res

@Timed
def solution(arr) :
	dup = defaultdict(int)

	for number in arr :
		dup[number] += 1

	# max_pair = (0, 0)
	# for key, value in dup.items() :
	res = max(dup, key = dup.get)

	return res
