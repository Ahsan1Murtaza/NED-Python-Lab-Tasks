# 1.   Construct the strings by using the string time format function strftime ()
# a) (Thursday, July 13 2018')
# b) ('09:40 PM Central Daylight Time on 07/13/2018')
# c) ('I will meet you on Thu July 13 at 09:40 PM.')

from datetime import datetime
import pytz

date_time=datetime(2018,7,13,21,40) # datetime(year, month, day, hour, minute)

# a)
str_a=date_time.strftime("%A, %B %d %Y")
print(str_a)


# Set the timezone to Central Daylight Time (CDT)
central = pytz.timezone('America/Chicago')
date_time = central.localize(date_time)

# b)
str_b = date_time.strftime("%I:%M %p %Z on %m/%d/%Y")
print(str_b)

# c)
str_c = date_time.strftime("I will meet you on %a %B %d at %I:%M %p")
print(str_c)