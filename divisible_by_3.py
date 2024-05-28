# Sum of Digits divisible by 3
# Implement a program to calculate sum of digits that are divisible by 3 in the
# given number
# nput -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of digits that are divisible by 3
# from 0 to 9 tell me the digits which are divisible by 3 ====> 3,6,9

def sum_of_digits():
    print(sum([int(i) for i in input() if int(i)%3 == 0]))

sum_of_digits()