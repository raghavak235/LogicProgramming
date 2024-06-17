# Given a string S, the task is to remove all the duplicates in the given string.
#
# Input Format
#
# a string from the user
#
# Constraints
#
# remove all duplicates
#
# Output Format
#
# a string without duplicates
#
# Sample Input 0
#
# hello
# Sample Output 0
#
# helo

def duplicate_string():
    n='hello'
    print(set(n))
    l = []
    for i in n:
        if i not in l:
            l.append(i)