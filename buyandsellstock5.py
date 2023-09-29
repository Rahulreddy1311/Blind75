prices = [int(x) for x in input("Enter prices: ").split()]
if not prices:
    print("Profit is 0")
else:
    lowest_price = prices[0]
    maximum_profit = 0
    for price in prices:
        profit_today = price - lowest_price
        maximum_profit = max(maximum_profit, profit_today)
        lowest_price = min(lowest_price, price)
    print("Profit:", maximum_profit)
