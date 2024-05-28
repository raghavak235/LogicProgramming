# Number of Occurrences
# Program to find number of occurrences of the given digit in the number n
# input ------> two numbers n and d
# constraints-> no constraints
# output -----> number of occurrences

#  Find the number of occurrence in number
#  EX: 3 in 1233 which is 2


def num_of_occurrence():
    n = input()
    d ={}
    for i in n:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)

    # Another Approach
    print(input().count(input()))
num_of_occurrence()