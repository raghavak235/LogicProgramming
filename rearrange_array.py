# rearrange an array in such an order that– smallest, largest, 2nd smallest, 2nd
# largest and on
# Implement a program to rearrange an array in such an order that-
# smallest,largest,2nd smallest, 2nd largest and so on.
# input ------> size and array elements
# con --------> no
# output -----> print the elements smallest, largest, 2nd smallest, 2nd largest and
# so on.

def rearrange_array():
    l=[1,4,5,2,3]
    n=5
    i =0
    j=n-1
    while i<=j:
        print(l[i]+l[j])
        i = i+1
        j = j+1

