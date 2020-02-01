def solution(items, capacity_of_bag) :
	dp = [[0 for j in range(capacity_of_bag+1)] for i in range(len(items) + 1)]

	for item in range(1, len(items) + 1) :
		curr_val, curr_weight = items[item-1][0], items[item-1][1]
		for capacity in range(1, capacity_of_bag + 1) :
			if curr_weight > capacity :
				dp[item][capacity] = dp[item - 1][capacity]
			else :
				including_item = curr_val + dp[item-1][capacity-curr_weight]
				excluding_item = dp[item-1][capacity]
				dp[item][capacity] = max(including_item, excluding_item)

	return [dp[-1][-1], contruct_items(items, dp)]

def contruct_items(items, dp) :
	res = []
	i, j = len(dp) - 1, len(dp[0]) - 1

	while i > 0 :
		if dp[i][j] != dp[i-1][j] :
			res.append(i-1)
			j -= items[i-1][1]
			i -= 1
		else :
			i -= 1
		if j == 0 :
			break

	return res[::-1]
