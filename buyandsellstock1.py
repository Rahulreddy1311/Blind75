class Solution:
    def maxProfit(self, prices):
        maximum_profit = 0
        prices = [int(x) for x in input("Enter prices: ").split()]
        if not prices:
            return maximum_profit
        lowest_price = prices[0]

        for day in range(len(prices)):
            lowest_price = min(prices[day], lowest_price)
            price_difference = prices[day] - lowest_price
            maximum_profit = max(price_difference, maximum_profit)
        return maximum_profit

solution = Solution()
result = solution.maxProfit([])
print("Profit:", result)
