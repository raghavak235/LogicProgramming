# You are given an array of integers, N of size array length. Find the absolute difference (i.e. diff>=0) between the largest and smallest prime numbers.
# Note:
# 1. if there are 1 or fewer prime numbers in array return 0.
# 2. the array may contain +ve and -ve numbers, ignore -ve numbers.
# 3. 1 and 0 are not prime.
#
# Input Format
#
# array size and array elements
#
# Constraints
#
# no
#
# Output Format
#
# absolute diff
#
# Sample Input 0
#
# 5
# 1 2 3 4 5
# Sample Output 0
#
# 3

def isprime(n):
    f=0
    for i in range(1,n+1):
        if n%i==0:
            f=f+1
    return f==2

def absolute_diff_primes():
    n=5
    l=[1,2,3,4,5]
    l.sort()
    l1=[]
    for i in l:
        if isprime(i):
            l1.append(i)

    l1.sort()
    if len(l1)>2:
        print(abs(l1[0]-l1[-1]))
    else:
        print(0)


