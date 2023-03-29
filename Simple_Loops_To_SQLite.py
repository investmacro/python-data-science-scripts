# -*- coding: utf-8 -*-

############## Simple Script to Store a Folder of CSVs into a SQLite Database
############## Using Pandas, glob & os

import sqlite3
import pandas as pd
import glob
import os

# Specify your own folders
db_save_to_folder = 'C:/MySaveFolder'
Spreadsheets_Folder = 'C:/MySpreadsheetsFolder'

#create a SQLite database connection
connection = sqlite3.connect('{}/BackUps.db'.format(db_save_to_folder))

# This will loop through your folder full of CSVs
for f in glob.glob("{}/*.csv".format(Spreadsheets_Folder)):
      base = os.path.basename(f)
      basename = os.path.splitext(base)[0]

      #read csv file
      spreadsheet_data = pd.read_csv(f)

      #create dataframe from csv data
      csv_df = pd.DataFrame(data=spreadsheet_data)
      csv_df.to_sql(basename, connection, if_exists='replace', index = False)

print('Loop is done!')

#commit changes
connection.commit()

#close connection
connection.close()
