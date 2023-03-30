# -*- coding: utf-8 -*-

#Running a Script from another Script

# For Example, You have a script in the Location Below
Script_Name_and_Location = 'C:/Users/Files/Location/Script_1.py'

# Now Run Script #1 from here
exec(open("C:/Users/Files/Location/Script_1.py").read())