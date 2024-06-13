# second smallest element in an array
# Implement a program to read array elements and find the second min element
# in an array.
# input -------> size and array elements.
# con ---------> size<100
# output ------> return second min element in array


def sec_min_element():
    l = [100,99,98,10,5,6,1,2]
    minimum = l[0]
    sminimum = l[1]
    for i in range(2, len(l)):
        if l[i] < minimum:
            sminimum = minimum
            minimum = l[i]
        elif minimum < l[i] < sminimum:
            sminimum = l[i]

    print(sminimum)

sec_min_element()
