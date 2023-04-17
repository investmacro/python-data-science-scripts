# -*- coding: utf-8 -*-

## Let's Drop a pandas dataframe column
## Let's rename a pandas dataframe column

import pandas as pd

## create a dataframe

## Create data for a dataframe
currencies = [('US Dollar', 'USD', 1),         
              ('Euro', 'EUR', 1.10),
              ('Australian Dollar', 'AUD', 0.75),
              ('Japanese Yen', 'JPY', 135), 
              ('British Pound', 'GBP', 1.22),
              ('New Zealand Dollar', 'NZD', 0.65),
              ('Swiss Franc', 'CHF', 1.03,)]

## Create the dataframe with columns
df = pd.DataFrame(currencies, columns=['Currencies','Symbols','Estimated Rate'])

print(df)
print('----------')

'''
## output is

           Currencies Symbols  Estimated Rate
0           US Dollar     USD            1.00
1                Euro     EUR            1.10
2   Australian Dollar     AUD            0.75
3        Japanese Yen     JPY          135.00
4       British Pound     GBP            1.22
5  New Zealand Dollar     NZD            0.65
6         Swiss Franc     CHF            1.03
'''

## Drop the 'Symbols' column from the dataframe

columns_to_drop = ['Symbols']

df.drop(columns_to_drop, inplace=True, axis=1)

print(df)
print('----------')

'''
## output is

           Currencies  Estimated Rate
0           US Dollar            1.00
1                Euro            1.10
2   Australian Dollar            0.75
3        Japanese Yen          135.00
4       British Pound            1.22
5  New Zealand Dollar            0.65
6         Swiss Franc            1.03
'''


####### Rename 'Estimated Rate' column to 'Forex Rate'

df.rename({'Estimated Rate': 'Forex Rate'}, axis=1, inplace=True)

print(df)
print('----------')

'''
## output is

           Currencies  Forex Rate
0           US Dollar        1.00
1                Euro        1.10
2   Australian Dollar        0.75
3        Japanese Yen      135.00
4       British Pound        1.22
5  New Zealand Dollar        0.65
6         Swiss Franc        1.03
'''
