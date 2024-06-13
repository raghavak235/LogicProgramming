# sum of even numbers in an array
# Implement a program to read an array elements and print sum of all even
# elements.
# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all even elements

def sum_of_even_numbers():
    l=[1,2,3,4,5]
    sum = 0
    for i in l:
        if i%2==0:
            print(i)
