# second largest element in an array
# Implement a program to read array elements and find the second max element
# in an array.
# input -------> size and array elements.
# con ---------> size<100
# output ------> return second max element in array

def second_largest_val_list():
    n = [1,2,3,4,5]
    largest = n[1]
    slargest = n[0]
    for i in range(2,len(n)):
        if n[i]> largest:
            slargest = largest
            largest = n[i]
        elif slargest < n[i] <= largest:
            slargest = n[i]
    print(slargest)

second_largest_val_list()
            