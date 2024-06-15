# Write a function that accepts an array of numbers (where each number appears three times except for one which appears only once) and finds that unique number in the array and returns it.
#
# Input Format
#
# array size and elements
#
# Constraints
#
# no
#
# Output Format
#
# return non-repeated number
#

def unique_ele_array():
    n=4
    l=[2,2,3,2]
    for i in l:
        if l.count(i) == 1:
            print(i)

unique_ele_array()