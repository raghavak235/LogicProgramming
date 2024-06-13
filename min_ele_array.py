# min element in an array
# Implement a program to read array elements and find the min element in an
# array.
# input -------> size and array elements.
# con ---------> size<100
# output ------> return min element

def min_elem_list():
    l=[5,1,2,4]
    min_ele = l[0]
    for i in l:
        if i < min_ele:
            min_ele = i
    print(min_ele)

min_elem_list()