# binary search
# Implement a program to search for an element in an array.
# input -------> size, array elements and element to search
# con ---------> size<100
# output ------> search for the given element

def binary_search():
    l=[1,3,5,7,9]
    value = 7
    begin_index=0
    end_index = len(l)-1
    while begin_index <= end_index:
        midpoint = (begin_index+end_index)//2
        midpoint_value = l[midpoint]
        if midpoint_value == value:
            return midpoint
        elif value < midpoint_value:
            end_index = midpoint -1
        else:
            begin_index = midpoint +1

    return None

print(binary_search())

