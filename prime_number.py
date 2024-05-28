# Prime Number or Not
# Write a program to check whether the given number is prime number or not.
# A number is said to prime if it is having only two factors. i.e. 1 and number
# itself.
# input ------> a number from the use
# constraint--> n>1
# output -----> true or false

# we should write a logic related to that number should be divisible by others

# you need divide number with all the numbers, if it has more than 2 factors 1, itself, it is not prime

def prime_number():
    n = int(input())
    if n > 1:
        for i in range(2, n+1):
            if n%i == 0:
                print('Not Prime')
                break
            else:
                print('prime')
                break


prime_number()