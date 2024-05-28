# Reverse Integer
# Given an integer x, return x with its digits reversed.
# input---------> a number from user
# constraint ---> n>=0
# output -------> reverse of the given number

def reverse_number():
    n = list(input())
    s=''
    for i in range(len(n)-1,-1,-1):
        s = s+n[i]
    print(s)

reverse_number()