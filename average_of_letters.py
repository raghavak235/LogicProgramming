# Find the Average of the Letters
# Create a function that returns the average of an array composed of letters.
# First, find the number of the letter in the alphabet in order to find the average
# of the array.
# A = 1
# B = 2
# C = 3
# D = 4
# E = 5
# average = total sum of all numbers / number of item in the set
# Return the result rounded to two decimal points.
# input -----> an array as string
# con -------> no
# output ----> Return the result rounded to two decimal points.

def average_nums_array():
    l = 'youarethebest'
    s= 0
    for i in l:
        s=s+(ord(i)-96)
    avg = s/len(l)
    print(round(avg,2))

average_nums_array()