class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        maximum_profit = 0
        lowest_price = prices[0]
        for price in prices:
            lowest_price = min(price, lowest_price)
            maximum_profit = max(price - lowest_price, maximum_profit)
        return maximum_profit
solution = Solution()
prices = [int(x) for x in input("Enter prices: ").split()]
result = solution.maxProfit(prices)
print("Profit:", result)
