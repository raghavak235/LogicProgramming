# sort the elements in an array ASC
# Implement a program to sort the given array elements in ASC order.
# input -----> size and array elements
# con -------> size<100
# output ----> sorted array in ASC

def sort_list():
    n=[9,8,7,1,2,3,4,5,6]
    sort_array=[]
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[j] < n[i]:
                temp = n[j]
                n[j] = n[i]
                n[i] = temp
    print(n)

sort_list()



