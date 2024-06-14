# sort an array of 0s, 1s and 2s
# Implement a program to read an array and sort array elements with 0s, 1s and
# 2s.
# input ------> size, array elements
# con --------> size<100
# output -----> print sorted elements

def sort_0s_1():
    l= [1,1,0,2,2]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] >= l[j]:
                l[i],l[j] = l[j], l[i]

    print(l)

sort_0s_1()