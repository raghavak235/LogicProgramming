# number of duplicate elements in array
# Implement a program to find the number of duplicate elements present in the
# given array.
# input ------> size, array elements
# con --------> size<100
# output -----> number of duplicate elements in the array

def duplicate_elems():
    l = [1,1,1,2,2,2,2]
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    print(d)
    print(max(d,key=d.get))

duplicate_elems()