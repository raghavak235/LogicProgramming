# Given an integer N and integer array A as the input, where N denotes the length of A write a program to find an integer the sum of all these product with successors.
#
# Input Format
#
# array size and elements
#
# Constraints
#
# no
#
# Output Format
#
# an int value
#
# Sample Input 0
#
# 5
# 1 2 3 4 5
# Sample Output 0
#
# 70

def product_successor():
    n=5
    l =[1,2,3,4,5]
    sum=0
    for i in l:
        sum = sum+ (i *(i+1))