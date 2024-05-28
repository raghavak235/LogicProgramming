# Find The Sequence Sum
# Given three integers i,j&k, a sequence sum to be the value of
# i+(i+1)+(i+2)..+j+(j-1)+(j-2)+..+k
# (increment from i until it equals to j,
# then decrement from j until equals k).
# Given values i,j,k.
# caluclate the sequence sum as described.
# int getSequenceSum(int,int,int);
# input -------> Three int values
# constraints--> no
# output ------> sum basd on given constraints

def sequence_sum():
    i = int(input())
    j = int(input())
    k = int(input())
    sum=0
    while i <=j:
        sum += i
        i = i+1
    while j!=k:
        j = j - 1
        sum += j
    print(sum)
    pass

sequence_sum()