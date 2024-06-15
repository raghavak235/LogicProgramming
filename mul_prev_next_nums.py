# Implement a program to update every array element with multiplication of previous and next numbers in an array.
#
# Input Format
#
# size and array elements
#
# Constraints
#
# no
#
# Output Format
#
# updated array

def mult_array():
    n=6
    l=[1,2,3,4,5,6]
    output = []
    output.append(l[1])
    for i in range(1, n-1):
        output.append(l[i-1]*l[i+1])
    output.append(l[-2])
    print(output)

mult_array()