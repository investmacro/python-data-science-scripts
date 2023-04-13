# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

############## Using Pandas isnull and Numpy .where to find missing values
############## import data from spreadsheet

data = pd.read_csv('C:/Spreadsheet-Folder')
df = pd.DataFrame(data=data)

## Find the mean missing values accross dataframe columns
mean_missing = df.isnull().mean()

print(mean_missing)

## Use numpy to see where missing values are
missing_values = np.where(pd.isnull(df))

print(missing_values)


