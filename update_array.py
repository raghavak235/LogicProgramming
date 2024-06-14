# update an element in an array
# Implement a program to update an element in the given array
# input ------> size,array elements and element to be updated (old element &
# new element)
# con---------> size<100
# output -----> return array after updating

def update_list():
    l=[1,2,3]
    for i in range(len(l)):
        if l[i] == 2:
            l[i] =0
    print(l)

update_list()