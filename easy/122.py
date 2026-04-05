'''You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
Find and return the maximum profit you can achieve.'''


def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0
