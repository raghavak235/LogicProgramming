# A Special two digit number
# A special two digit number is a number such that when
# the sum of its digits is added to the product of its digits, the result should be
# equal to the original two-digit number.
# Implement a program to accept a two digit number and check whether it is a
# special two digit number or not.
# input -----> a two digit number
# constraint-> 10<=n<=99
# output ----> special two digit number or not

def special_2digit():
    n = list(input())
    if 10 <= int(''.join(n)) <= 99:

        sum_n = sum([int(i) for i in n])
        product_n = int(n[0]) * int(n[1])
        if sum_n + product_n == int(''.join(n)):
            print('Special 2 digit number')
        else:
            print('Not')
    else:
        print('invalid')

special_2digit()