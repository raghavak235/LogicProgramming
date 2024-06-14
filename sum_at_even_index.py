# sum of elements available at even index
# Implement a program to find the sum of elements avaiable at even index
# locations in an array.
# input ----> size and array elements
# con ------> no

def sum_even_index():
    l =[1,2,3,4,5]
    s=0
    for i in range(len(l)):
        if i%2==0:
            s += l[i]
    print(s)

sum_even_index()