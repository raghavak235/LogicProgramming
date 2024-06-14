# sum of elements available at odd index
# Implement a program to find the sum of elements avaiable at odd index
# locations in an array.
# input ----> size and array elements
# con ------> no
# output ---> print sum value

def sum_odd_index():
    l = [1, 2, 3, 4, 5]
    s = 0
    for i in range(len(l)):
        if i % 2 != 0:
            s += l[i]
    print(s)
