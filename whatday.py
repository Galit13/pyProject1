from datetime import datetime
from datetime import date
import time
from enum import Enum


class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


# Initialize the date parameters
day = datetime.now().day
month = 8
year = int(input("Enter a year: "))
date = date(year, month, day)

print("Processing.", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")

# Get the day name from the Week enum
weekday = date.isoweekday()
weekday = Week(weekday).name
print(date, "was a", weekday)