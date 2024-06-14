# Sum of adjacent Distances
# Write a program to calculate and return sum of distances between the
# adjacent numbers in an array of +ve integers.
# input -------> size and array elements
# con ---------> no
# output ------> an int value

def sum_adjacent_dist():
    l =[1,2,3,4,5]
    s=0
    for i in range(0,len(l)-1):
        # print(l[i+1]-l[i])
        s = s + (l[i+1]-l[i])

    print(s)

sum_adjacent_dist()