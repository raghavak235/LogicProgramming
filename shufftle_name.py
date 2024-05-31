# Shuffle the Name
# Problem Statement: Create a function/method that accepts a string (of
# person’s first and last name) and returns a string with in first and last name
# swapped).
# Input: two space separated strings
# Constraints: No
# Output: return last name followed by first name

def shuffle_name():
    fullname=input().split()
    print(fullname[1]+fullname[0])
