# sum of two arrays
# Implement a program to find the sum of two arrays and display the result array
# input -------> size and array elements
# con ---------> no
# output ------> print resultent array

def add_two_arrays():
    l=[1,2,3]
    m=[1,2,3]
    out=[]
    for i in range(len(l)):
        out.append(l[i]+m[i])
    print(
        out
    )

add_two_arrays()