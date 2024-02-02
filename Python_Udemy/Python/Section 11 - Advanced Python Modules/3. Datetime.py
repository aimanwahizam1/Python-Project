# ---------------------------------------------------------------------------- #
#                                   Datetime                                   #
# ---------------------------------------------------------------------------- #

import datetime

my_time = datetime.time(2,20)
""" print(my_time)
print(my_time.hour)
print(my_time.minute) """

today = datetime.date.today()
""" print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime()) """

my_datetime = datetime.datetime(1998,9,12,4,12)
print(my_datetime.ctime())

# You can replace a specific value
my_datetime = my_datetime.replace(year=1999)
print(my_datetime.ctime())

# -------------------------------- Arithmetic -------------------------------- #

# You can perform arithmetic on date and datetime
date1 = datetime.date(2025,2,1)
date2 = datetime.date.today()

print(date1-date2)

datetime1 = datetime.datetime(2025,2,1,22)
datetime2 = datetime.datetime.now()
result = datetime1-datetime2
print(result)
print(result.total_seconds())