# Return the Sum of the Two Smallest Numbers
# Create a function that takes an array of numbers and returns the sum of the
# two lowest positive numbers.
# input -------> size and an array
# con ---------> Dn't count negative numbers
# output ------> sum of two smallest positive numbers

def sum_2_posnums():
    l=[5,4,3,2,1]
    l.sort()
    s= 0
    s = l[0] + l[1]
