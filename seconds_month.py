# תרגיל 2 – מספר שניות בחודש
from enum import Enum


class Month(Enum):
    SEP = 30
    OCT = 31
    NOV = 30
    DEC = 31
    JAN = 31
    FEB = 28
    MAR = 31
    APR = 30
    MAY = 31
    JUN = 30
    JUL = 31
    AUG = 31


month = input("Enter month name in 3 capital letters: ")
seconds_in_month = Month[month].value * 24 * 3600
print("In", month, "there are", seconds_in_month, "seconds")