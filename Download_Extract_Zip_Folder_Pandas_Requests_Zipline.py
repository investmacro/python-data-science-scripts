# -*- coding: utf-8 -*-

# import our libraries
import requests, zipfile
import io
import pandas as pd

# use requests to get the zip file from our link
r = requests.get('https://www.example.com/files/our_file.zip')

# use zipfile to read zip
z = zipfile.ZipFile(io.BytesIO(r.content))

# open the file inside the zip file, in this file we know we have an spreadsheet named 'my_sheet_download'
my_file = pd.ExcelFile(z.open('my_sheet_download.xls'))

# parsing the XLS file into a dataframe
my_file.sheet_names
df = my_file.parse('XLS')

# Saving new dataframe as a CSV file to folder
save_folder = 'C:/My_Folder_Location'
df.to_csv('{}/My_New_CSV_File.csv'.format(save_folder), index=False, date_format='%m-%d-%Y', header=True)
