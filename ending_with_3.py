# sum of elements in an array ending with 3
# Implement a program to read an array elements and print sum of elements
# ending with 3 in array.
# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of elements ending with 3

def ending_with_3():
    n = list((input()))
    s=0
    for i in n:
        if i.endswith(3):
            s=int(i)
