# -*- coding: utf-8 -*-

import glob
import os

## directory of CSVs to loop through
directory = 'C:/MyFolder'

## Empty List you will append to
symbols = []

## for loop starts, loops through CSVs in a directory
for f in glob.glob("{}/*.csv".format(directory)): 
    
     ## get the csv file path, isolate just the file name as basename
     base = os.path.basename(f)
     basename = os.path.splitext(base)[0]
     
     ## append the file name to the symbols list
     symbols.append(basename)
     
## print the list
print(symbols)

