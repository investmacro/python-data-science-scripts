# -*- coding: utf-8 -*-

################ Current Datetime Formats (Years,Months,Days,Hours,Minutes,Seconds) 
import datetime
now = datetime.datetime.now()

year = '{:02d}'.format(now.year)
month = '{:02d}'.format(now.month)
day = '{:02d}'.format(now.day)
hour = '{:02d}'.format(now.hour)
minute = '{:02d}'.format(now.minute)
second = '{:02d}'.format(now.second)

publish_date = '{}-{}-{}T{}:{}:{}'.format(year, month, day, hour, minute, second)
publish_date1 = '{}_{}_{}_{}:{}:{}'.format(year, month, day, hour, minute, second)
publish_date2 = '{}-{}-{}'.format(month, day, year,)

print(publish_date)
print(publish_date1)
print(publish_date2)