# number of even and odd elements
# Implement a program to find number of even and odd elements in the given
# array
# input -------> size and array elements
# con ---------> no
# output ------> print number of even and odd elements line by line

def num_of_even_odd():
    l=[1,2,3,4,5]
    es=0
    os=0
    for i in l:
        if i%2==0:
            es = es+1
        else:
            os = os +1