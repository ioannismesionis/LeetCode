# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:

# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


class Solution:
    def maxProfit(self, prices):
        # buy = 1 --> we can buy
        buy = 1
        profit = 0

        length = len(prices)
        for i in range(0, length - 1):
            # Check if we want to buy
            if (buy == 1) & (prices[i] < prices[i+1]):
                buy_val = prices[i]
                buy = 0
            # Check if we want to sell
            elif (buy == 0) & (prices[i] > prices[i+1]):
                sell_val = prices[i]
                profit += sell_val - buy_val
                buy = 1
        # If we haven't sell by the end of code
        # sell on the last price
        if buy == 0:
            sell_val = prices[-1]
            profit += sell_val - buy_val

        return profit


nums = [7, 1, 5, 3, 6, 4]
solution = Solution()
print("Max profit is:", solution.maxProfit(nums))
