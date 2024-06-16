# Write a program to find the absolute difference between the original number and its reserved number.
#
# Input Format
#
# a number from the user
#
# Constraints
#
# no
#
# Output Format
#
# absolute difference
#
# Sample Input 0
#
# 245
# Sample Output 0
#
# 297

def difference():
    n = 245
    print(abs(n-n[::-1]))

