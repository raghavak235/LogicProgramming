# Extract Digits from the number
# Implement a program to extract digits from the given number
# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print digits in line sep by space

def digits_from_num():
    n = int(input())
    while n != 0:
        d = n % 10
        print(d, end=' ')
        n = n//10

digits_from_num()