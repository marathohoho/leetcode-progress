'''

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

# importing time module
from time import time
class Timed:
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {} seconds\n".format(end_time-start_time))
        return result

	# def __init__(self, func):
	# 	self.func = func

	# def __call__(self, *args, **kwargs) :
	# 	start = perf_counter()
	# 	result = self.func(*args, **kwargs)
	# 	end = perf_counter()
	# 	elapsed = end - start

	# 	args_ = [str(a) for a in args]
	# 	kwargs_ = [f'{k}={v}' for k, v in kwargs.items()]
	# 	all_args = args_ + kwargs_
	# 	args_str = ','.join(all_args)
	# 	print(f'{self.func.__name__}({args_str}) took {elapsed:.6f}s to run')

	# 	return result

class Solution :

	@Timed
	def decodeWays(self, s) :
		if not s :
			return 0

		dp = [0] * (len(s)+1)
		dp[0] = 1

		for i in range(1, len(s) + 1) :
			if s[i-1] != '0' :
				dp[i] += dp[i-1]
			if i != 1 and s[i-2:i] < '27' and s[i-2:i] >'09' :
				dp[i] += dp[i-2]

		return dp[len(s)]

