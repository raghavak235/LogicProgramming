# Sort only First half of the elements
# Implement a program to sort only first half of the array and keep remaining
# elements as original.
# input ------> size and array elements
# con --------> no
# output -----> sort only first half of the array

def sort_half():
    n=5
    l=[3,2,1,4,5]
    for i in range(0, len(l)//2):
        for j in range(i+1, len(l)//2):
            if l[i]> l[j]:
                l[i],l[j]=l[j],l[i]
    print(l)


sort_half()