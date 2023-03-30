# -*- coding: utf-8 -*-

# Get just the symbol of the stock from the string: AAPL-EarningsPerShare

Symbol = 'AAPL-EarningsPerShare'.split('-')[0]

print(Symbol)

# Let’s get the second part of the string (EarningsPerShare)

Symbol_Part2 = 'AAPL-EarningsPerShare'.split('-')[1]
print(Symbol_Part2)

# Example #2
# In this next example, we have a date like this: November_27_1942

Month = 'November_27_1942'.split('_')[0]
Day = 'November_27_1942'.split('_')[1]
Year = 'November_27_1942'.split('_')[2]

print(Month)
print(Day)
print(Year)