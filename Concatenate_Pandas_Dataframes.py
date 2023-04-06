# -*- coding: utf-8 -*-

# script to concatenate 2 spreadsheets together, output as 1 spreadsheet

# import our libraries
import pandas as pd

# csv spreadsheet #1 location
spreadsheet = 'C:/Location/spreadsheet.csv'
     
# Create a dataFrame from spreadsheet #1
data_1 = pd.read_csv(spreadsheet)
df1 = pd.DataFrame(data=data_1)
     
# csv spreadsheet #2 location
spreadsheet_2 = 'C:/Location/spreadsheet_2.csv'

# Create a dataFrame from spreadsheet #2
data_2 = pd.read_csv(spreadsheet_2)
df2 = pd.DataFrame(data=data_2)
     
# Concatenate the 2 dataFrames
concatenated_df = pd.concat([df1, df2], axis=0)

# Output the new combined dataFrame into a csv
concatenated_df.to_csv('C:/Location/Concatenated_Spreadsheet.csv', index=False, header=True,)

# if you want to remove duplicate entries from a column such as Dates
combined_without_duplicates = concatenated_df.drop_duplicates(['Date'])
     
# Re-Output to Updated Folder
combined_without_duplicates.to_csv('C:/Location/Concatenated_Spreadsheet_No_Duplicates.csv', index=False, header=True,)