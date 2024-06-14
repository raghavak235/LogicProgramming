# array reverse
# Write a program to reverse the elements present in an array
# input ------> size, array elements
# con --------> size<100
# output -----> return array in reverse

def reverse_list():
    l=[1,2,3,4]
    l[::-1]
    rev_list = []
    for i in range(len(l)-1,-1, -1):
        rev_list.append(l[i])
    print(rev_list)


reverse_list()