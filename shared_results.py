# Shared Digits
# Create a function that returns true if each pair of adjacent numbers in an array
# shares at least one digit and false otherwise.
# input --------> array size and array elements
# con ----------> no
# output -------> true or false

def adjacent_digits():
    n=5
    l=[12, 13, 17, 19, 79]
    c=0
    for i in range(n-1):
        for j in str(l[i]):
            if j in l[i+1]:
                c=c+1
                break
    print(str(c==n-1).lower())
