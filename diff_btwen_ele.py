# Difference between two arrays
# Implement a program to find the difference between two arrays
# input -------> size and array elements
# con ---------> no
# output ------> print difference between two arrays as third array


def difference_2_arrays():
    l=[1,2,3]
    m=[1,2,3]
    output=[]
    for i in range(len(l)):
        output.append(l[i]-m[i])