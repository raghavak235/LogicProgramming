# increment every element in an array by one unit
# Implement a program to increment every element by one unit in array.
# input ------> size, array elements
# con --------> size<100
# output -----> increment each element by one unit

def increment_every_element():
    l = [1,2,3]
    for i in range(len(l)):
        l[i] = l[i]+1

    print(l)

increment_every_element()
