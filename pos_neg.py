# Positives and Negatives
# Create a function which validates whether a given array alternates between
# positive and negative numbers.
# nput --------------> an array size and array
# con ----------------> no
# output -------------> true or false

def pos_neg():
    l=[3, -2, 5, -5, 2, -8]
    flag=True
    # verify If both numbers have the same sign
    for i in range(len(l)-1):
        if l[i] >0 and l[i+1] >0:
            flag=False
            break
        elif l[i] <0 and l[i+1] <0:
            flag=False
            break