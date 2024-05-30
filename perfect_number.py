# Perfect Number
# Create a function that tests whether an integer is a perfect number.
# A perfect number is a number that can be written as sum of its factors.
# (equal to sum of its proper divisors) excluding the number itself.
# input ------> a number from the user
# constraint -> n>0
# output -----> true or false

def perfect_number():
    n = int(input())
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum +=i
    print('Perfect Number')if sum == n else print('Not')


perfect_number()