prices = [int(x) for x in input("Enter prices: ").split()]
if not prices:
    print("Profit is 0")
else:
    lowest_price = prices[0]
    maximum_profit = 0
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        elif price - lowest_price > maximum_profit:
            maximum_profit = price - lowest_price
    print("Profit:", maximum_profit)
