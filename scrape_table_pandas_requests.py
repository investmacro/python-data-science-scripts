# -*- coding: utf-8 -*-

#  Scrape website table using Pandas & Requests

import pandas as pd
import requests

# chosen website table
webpage = 'https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue'

# use requests to get webpage
page = requests.get(webpage)
# use pandas to read the html 
manufacturing_data = pd.read_html(page.text)

# specify which table we want to get (if more than 1 table on page), 0 is the first table
first_table = manufacturing_data[0]

# print the first 15 rows of table
print(first_table[0:15])

# Now Save to a CSV file

# specify your folder location 
data_folder = 'C:/Users/Name/Folder_Location'

# save to csv
first_table.to_csv('{}/manufacturing.csv'.format(data_folder), index=False)