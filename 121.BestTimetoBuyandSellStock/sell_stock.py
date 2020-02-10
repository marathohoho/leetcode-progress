"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


def profit(arr) :
	if len(arr) < 2  :
		return 0

	max_profit = 0
	current_minimum = arr[0]

	for i in range(1, len(arr)):
		max_profit = max(max_profit, arr[i] - current_minimum)

		current_minimum = min(current_minimum, arr[i])

		if max_profit < 0 :
			return 0
	return max_profit

if __name__ == "__main__":
	print(profit([7, 10, 15, 20]))
	print(profit([7, 1, 5, 3, 6, 4]))
	print(profit([3,3,5,0,0,3,1,4]))

