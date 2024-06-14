# Eliminate Odd Numbers within an Array
# Create a function that takes an array of numbers and returns only the even
# values.
# Return all even numbers in the order they were given.
# All test cases contain valid numbers ranging from 1 to 3000.
# input -----> size and an array
# con -------> no
# output ----> remove all odd numbers and print

def eliminate_odd_nums():
    l=[1,2,3,4,5]
    for  i in l:
        if i%2==0:
            print(i)