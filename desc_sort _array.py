# sort the elements in an array DESC
# Implement a program to sort the given array elements in DESC order.
# input -----> size and array elements
# con -------> size<100
# output ----> sorted array in DESC

def desc_sort_list():
    n = [1,2,3,4,5,6,7,8,9]
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[j] > n[i]: # here we are verifying if the second value is > than 1st because we need to sort DESC
                temp=n[j]
                n[j]=n[i]
                n[i]=temp

    print(n)

desc_sort_list()