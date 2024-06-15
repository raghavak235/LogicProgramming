# given an array of size n, write a function to rearrange the numbers of the array in such that even and odd numbers are arranged alternatively in increasing order.
#
# Input Format
#
# array size n and elements
#
# Constraints
#
# no
#
# Output Format
# updated array


def arrange_even_odd():
    l1=[1,2,3,4]
    n=4
    l2=[]
    l3=[]
    l1.sort()
    for i in l1:
        if i%2==0:
            l2.append(i)
        else:
            l3.append(i)
    index=0
    while index < n//2:
        print(l2[index],l3[index], end=' ')
        index = index+1

arrange_even_odd()        