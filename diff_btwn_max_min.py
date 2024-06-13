# diff between largest and smallest element in array
# Implement a program to read array elements and find the difference between
# max and min element in an array.
# input -------> size and array elements.
# con ---------> size<100
# output ------> return difference between max and min element.

def max_min_diff():
    l=[9,8,7,6,1,2,3,4,5]
    l_sort = sorted(l)
    print(max(l_sort)-min(l_sort))
