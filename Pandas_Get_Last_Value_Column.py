# -*- coding: utf-8 -*-

import pandas as pd

## Getting the Last Value in a Dataframe Column using iloc

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

## Get the Last value in the Currencies Column
last_currency = df['Currencies'].iloc[-1]

## Get the Second to Last value in the Currencies Column
second_to_last_currency = df['Currencies'].iloc[-2]

print('The last currency is the '+last_currency)

print('The second to last currency is the '+second_to_last_currency)
