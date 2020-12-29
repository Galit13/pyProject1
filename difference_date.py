from datetime import datetime
from datetime import date
import random

MONTH_NOW = datetime.now().month
YEAR_NOW = datetime.now().year
MONTH_RANDOM = random.randint(1, 12)
YEAR_RANDOM = random.randint(1980, YEAR_NOW)
#print(MONTH_RANDOM)
#print(YEAR_RANDOM)

month_difference = MONTH_NOW - MONTH_RANDOM
year_difference = YEAR_NOW - YEAR_RANDOM

if month_difference < 0:
    if YEAR_RANDOM == YEAR_NOW:
        month_difference = MONTH_RANDOM - MONTH_NOW
    else:
        year_difference = year_difference - 1
        month_difference = 12 - (MONTH_RANDOM - MONTH_NOW)

print(month_difference, "/", year_difference)
