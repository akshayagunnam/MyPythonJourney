"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        days = len(prices)
        min_price = prices[0]; profit = 0
        for i in range(1, days):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = max(prices[i] - min_price, profit)
        return profit
