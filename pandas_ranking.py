# -*- coding: utf-8 -*-

# Let's Create a Pandas DataFrame of 10 Large Cap Stocks

# import the Pandas library
import pandas as pd

# Our Stocks Data with Symbols, Dividends and PE Ratios
stocks = {'Symbol': ['AAPL','ABBV','V','JNJ','PG','KO','LLY','MA','MCD','MRK'],
'Dividend Yield': ['0.66','3.84','0.75','2.66','2.74','2.96','1.09','0.63','2.01','2.79'],
'PE Ratio': ['29.1','73.4','27.5','24.1','20.1','21.5','50.2','27.4','38.2','14.6']}

#### Creating 2 DataFrames for easy visualization purposes

# Dividend Yield Dataframe
stock_divyield = pd.DataFrame(stocks)

# PE Ratio Dataframe
stock_peratio = pd.DataFrame(stocks)

#1 Creating new column for rankings in Dividend Yield Dataframe
stock_divyield['Dividend_Yld_Rank'] = stock_divyield['Dividend Yield'].rank(ascending=True, pct=True)

#2 Sorting the rankings 
stock_divyield = stock_divyield.sort_values(['Dividend_Yld_Rank'], ascending=False)

# Print Dividend Yield Dataframe
print(stock_divyield)

#1 Creating new column for PE Ratio rankings in PE Ratio Dataframe
# We want to rank the lowest PE Ratio as the best or 1
stock_peratio['PE_Ratio_Rank'] = stock_peratio['PE Ratio'].rank(ascending=False, pct=True)

#2 Sorting the PE Ratio rankings 
stock_peratio = stock_peratio.sort_values(['PE_Ratio_Rank'], ascending=False)

# Print PE Ratio Dataframe
print(stock_peratio)