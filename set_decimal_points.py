# -*- coding: utf-8 -*-

import pandas as pd

## Create data for a dataframe, third column has values with many decimal places
currencies = [('US Dollar', 'USD', 1.558745),         
              ('Euro', 'EUR', 1.1098766),
              ('Australian Dollar', 'AUD', 0.756789),
              ('Japanese Yen', 'JPY', 135.65678), 
              ('British Pound', 'GBP', 1.226546),
              ('New Zealand Dollar', 'NZD', 0.6532345),
              ('Swiss Franc', 'CHF', 1.0367098,)]

## Create a dataframe with columns
df = pd.DataFrame(currencies, columns=['Currencies','Symbols','Estimated Rate'])

## Will see 'Estimated Rate' column with many decimal places
print(df['Estimated Rate'])

## Change the 'Estimated Rate' column to 2 decimal places
df['Estimated Rate'] = df['Estimated Rate'].round(decimals = 2)

print(df['Estimated Rate'])

## Change just the last value of 'Estimated Rate' column to 2 decimal places
last_value_two_decimals = df['Estimated Rate'].iloc[-1].round(decimals = 2)

print(last_value_two_decimals)
