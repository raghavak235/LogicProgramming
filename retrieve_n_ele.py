# Retrieve the Last N Elements
# Write a function that retrieves the last n elements from an array.
# input -------> size, an array and N value
# con ---------> return 0 if n exceeds size of the array
# output ------> last N elements

def last_n_values():
    l=[1,2,3,4,5,6]
    n=6
    m=3
    print(l[n-m:])

last_n_values()