from time import time

class Timed :
	def __init__(self, fn) :
		self.fn = fn
	def __call__(self, *args, **kwargs) :
		start = time()
		res = self.fn(*args, **kwargs)
		end = time()

		print(f'It took {end - start} seconds')
		return res

@Timed
def solution(n) :
	if n == 0 or n == 1 :
		return 1
	dp = [0] * (n+1)
	dp[0] = 1
	dp[1] = 1

	for i in range(2, n+1) :
		dp[i] = dp[i-1] + dp[i-2]
	return dp[-1]
