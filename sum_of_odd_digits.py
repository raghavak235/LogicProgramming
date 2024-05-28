# Sum of odd Digits
# Implement a program to calculate sum of odd digits present in the given
# number
# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of odd digits

def sum_of_odd_digits():
    print(sum([int(i) for i in input() if int(i)%2 !=0]))

sum_of_odd_digits()