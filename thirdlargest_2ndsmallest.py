# Given an integer array and an integer N denoting the array length as input. your task is to return the sum of third largest and second minimum elements of the array.
#
# Input Format
#
# array size and array elements
#
# Constraints
#
# no
#
# Output Format
#
# an int value

# 1st min: a[1-1] 1st max: a[n-1]
# 2nd min: a[2-1] 2nd max: a[n-2]
# 3rd min: a[3-1] 3rd max: a[n-3]
# formula: a[n-3]+a[2-1]

def thirdlargest_2ndsallest():
    n=5
    l=[5,4,3,1,2]
    l.sort()
    print(l[n-3] + l[2-1])