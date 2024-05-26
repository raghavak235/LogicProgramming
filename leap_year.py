# To check whether the given number is leap year or not.
# input------> year from the user
# constraint-> no constraint
# output-----> leap year or not leap year

# A year is said to be leap year if it follows the following conditions
# 1. the year should be divisible by 4 and should not be divisible by 100  or the year should be divisible by 400.

def leap_year():
    year = int(input('Enter the year'))
    if (year%400 ==0) or (year%100!=0 and year%4==0):
        print("leap year")
    else:
        print("not leap year")


leap_year()
