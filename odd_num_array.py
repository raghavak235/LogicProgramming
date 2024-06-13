# sum of odd numbers in an array
# Implement a program to read an array elements and print sum of all odd
# elements.
# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all odd elements

def sum_odd_array():
    l =[1,2,3,4,5]
    print(sum([i for i  in l if i%2!=0]))