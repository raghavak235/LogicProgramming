# Array of multiples
# Implement a program to create an array with n elements by taking multiples of
# m.
# input -----> m and n
# con--------> size of the array must be n
# output ----> return an array with n elements which contains multiples of m.


def multiples_array():
    m=7
    n = 5
    mul=[]
    for i in range(1, n+1):
        mul.append(m * i)