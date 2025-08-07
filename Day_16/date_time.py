# Exercises: Day 16

from datetime import datetime
from datetime import timedelta

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

print()

# 1. Get the current day, month, year, hour, minute and timestamp from datetime
# module

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print("Format the current date" ,now.strftime("%m/%d/%Y, %H:%M:%S"))

# 3. Today is 5 December, 2019. Change this time string to time.
new_year = datetime(2019, 12, 5)

# 4. Calculate the time difference between now and new year.
print(now - new_year)

# 5. Calculate the time difference between 1 January 1970 and now.
print(datetime(1970, 1, 1) - now)

