def solution(str1, str2) :
	# create a dp table with len(str1) + 1 * len(str2) + 1

	dp = [["" for j in range(len(str1) + 1)] for i in range(len(str2) + 1)]

	for i in range(1, len(str2) + 1) :
		for j in range(1, len(str1) + 1) :
			# make dp conditions
			if str1[j-1] == str2[i-1] : # we have a common letter
				# append the dp cell with previous occurence (if we do not take into account he last letter from both strings)
				dp[i][j] += dp[i-1][j-1] + str2[i-1]
			else :
				# we need to append the longest of the subsequences from the two strings
				dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]

	print(dp)
	return dp[-1][-1]


"""
Time : O(m * n) m, n - lengths of strings

Space : O(m * n) as well due to dp matrix
"""
