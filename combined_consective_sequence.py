# Combined Consecutive Sequence
# Write a function that returns true if two arrays, when combined, form a
# consecutive sequence.
# A consecutive sequence is a sequence without any gaps in the integers,
# e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
# input --------> two array sizes and array elements
# con ----------> no
# output -------> true or false

def combined_consecutive_number():
     l=[12, 13, 17, 19]
     m=[14 ,16, 15, 18]
     n1,n2=4,4
     output=l+m
     output.sort()
     c=0
     for i in range(len(output)-1):
          if output[i]+1 == output[i+1]:
               c=c+1