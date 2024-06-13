# sum of palindrome numbers in an array
# Implement a program to read an array elements and print sum of all
# palindrome numbers in array.
# input -------> size of the array and array elements
# con ---------> size<100
# # output ------> sum of all palindrome numbers

def palindrome(n):
    n = [121, 122, 123]
    s=0
    for i in n:
        if i==i[::-1]:
            s=s+i
