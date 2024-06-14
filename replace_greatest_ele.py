# replace every element with the greatest element on its right side
# Implement a program to read an array and replace every element with the
# greatest element on its right side.
# input ------> size, array elements
# con --------> size<100
# output -----> print updated array elements

def replace_greatest_ele():
    l= [1,2,3,4,5]
    max_l = max(l)
    for i in range(len(l)):
        l[i]=max_l
