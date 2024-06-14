# print unique elements in array
# Implement a program to find the unique elements present in the given array.
# input ------> size, array elements
# con --------> size<100
# output -----> print unique elements present in the array

def unique_ele():
    l=[1,1,2,3]
    for i in l:
        if l.count(i) == 1:
            print(i, end=' ')


unique_ele()