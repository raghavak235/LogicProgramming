# Paliandrome Number
# Program to check whether the given number is paliandrome or not
# input -----> a number from the user
# constraint-> n>0
# output ----> Yes or No

#  EX: 123 = 321

def palindrome():
    n= input()
    if n == n[::-1]:
        print('Yes')
    else:
        print('No')