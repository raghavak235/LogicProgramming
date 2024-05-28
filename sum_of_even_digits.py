# Sum of even Digits
# Implement a program to calculate sum of even digits present in the given
# number
# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of even digits

def sum_of_even_digits():
    n = int(input('Enter your number'))
    s=0
    while n != 0:
        d = n%10
        if d%2 ==0:
            s = s +d
        n = n//10
    print(s)

sum_of_even_digits()
