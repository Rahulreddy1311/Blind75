prices = [int(x) for x in input("Enter prices: ").split()]
if not prices:
    print("Profit is 0")
else:
    lowest_price = prices[0]
    maximum_profit = 0
    i = 0
    while i < len(prices):
        if prices[i] < lowest_price:
            lowest_price = prices[i]
        elif prices[i] - lowest_price > maximum_profit:
            maximum_profit = prices[i] - lowest_price
        i += 1
    print("Profit:", maximum_profit)
