# Max Occurring Character
# Given a string, implement a program to find max occurring character in the
# given string
# input -------> A string from the user.
# constraints--> No
# output ------> max occurring characterMax Occurring Character
# Given a string, implement a program to find max occurring character in the
# given string
# input -------> A string from the user.
# constraints--> No
# output ------> max occurring character

def max_returning_char():
    n  =input()
    dict_N={}
    for i in n:
        if i not in dict_N:
            dict_N[i] =1
        else:
            dict_N[i] +=1
    print(dict_N)

    char = n[0]
    max_count = dict_N[n[0]]
    for k, v in dict_N.items():
        if v > max_count:
            max_count= v
            char=k
    print(char)

    #Another Implementation
    from collections import Counter
    s=input()
    r= Counter(s)
    print(r)
    # If you want to use max value wrt to key in dict, use key=r.get
    print(max(r, key=r.get))




max_returning_char()