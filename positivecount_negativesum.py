# Positive Count / Negative Sum
# Create a function that takes an array of positive and negative numbers.
# Return an array where the first element is the count of positive numbers and
# the second element is the sum of negative numbers.
# input -------> size and an array
# con ---------> If given an empty array, return an empty array and 0 is not
# positive.
# output ------> two space seperated int values

def sum_of_pos_neg():
    l=[1,2, 3, 4 ,5 ,6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    ps,ns=0,0
    for i in l:
        if i>0:
            ps+=1
        else:
            ns +=i

    print(ps,ns)
sum_of_pos_neg()