# War of Numbers
# There is a great war between the even and odd numbers.
# Many numbers already lost thier life in this war and its your task to end this.
# You have to determine which group sums larger. the even, or the odd, the
# larger group wins.
# Create a function that takes an array of integers , sums the even and odd
# numbers seperately,
# then return the difference between sum of even and odd numbers.
# input --------> number and array elements
# constraint ---> no
# output -------> difference between sum of even and odd numbers

def even_odd_war():
    n  = input()
    l = [int(i) for i in input().split()]
    sum_even, sum_odd = 0,0
    for i in l:
        if i%2 == 0:
            sum_even += i
        else:
             sum_odd+= i
    # print(sum_even, sum_odd)
    print(abs(sum_even -sum_odd))


even_odd_war()