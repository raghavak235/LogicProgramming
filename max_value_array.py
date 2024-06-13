# max element in an array
# Implement a program to read array elements and find the max element in an
# array.
# input -------> size and array elements.
# con ---------> size<100
# output ------> return max element

def max_value_list():
    l=[1,2,3,4,5,6,7,8,9]
    max_ele=l[0]
    for i in l:
        if i > max_ele:
            max_ele = i
    print(max_ele)


max_value_list()