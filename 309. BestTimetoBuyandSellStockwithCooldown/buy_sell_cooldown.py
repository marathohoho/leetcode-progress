"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

def stock(prices) :
	if len(prices) < 2 :
		return 0

	buy_prev = -1 * prices[0]
	sell_prev = 0
	hold_prev = 0

	for i in range(1, len(prices)) :
		buy = max(buy_prev, hold_prev - prices[i])
		sell = max(sell_prev, prices[i] + buy_prev)
		hold = max(hold_prev, sell_prev, buy_prev)

		buy_prev, sell_prev, hold_prev = buy, sell, hold

	return max(sell, hold)


if __name__ == "__main__":
	print(stock([1,2,3,0,2]))
