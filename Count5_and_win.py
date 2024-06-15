# Count 5s And Win
# Arun is obsessed with primes, especially five.
# He considers a number to be luckiest if it has the highest number of five in it.
# If two numbers have the same frequency of five,
# Arun considers the last occurence of them to be luckiest, and if there is no five
# in any number,
# the first given number is considered luckiest.
# Help him choose the luckiest number.
# input -----------> array size and elements
# con -------------> no
# output ----------> return luckiest number

def count_5s():
    n=5
    l=[]
    c=0
    sc=0
    for i in l:
        x=str(i).count('5')
        if c<=x:
            c=x
            element=i
        if x==0:
            sc=sc+1
    if sc !=n:
        print(element)
    else:
        print(l[0])


