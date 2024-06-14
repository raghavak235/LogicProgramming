# Mini Peaks
# Write a function that returns all the elements in an array
# that are strictly greater than their adjacent left and right neighbors.
# input ------> size, an array
# con---------> Do not count boundary numbers, since they only have one
# left/right neighbor.
# output -----> an array

def adjacent_numbers():
    n = [1,2,3,4,5]
    for i in range(1, len(n)-1):
        if n[i]>n[i-1] and n[i]>n[i+1]:
            print(n[i])