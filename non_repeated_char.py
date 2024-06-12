# first non-repeated character
# Program to find first non-repeated character
# input----> a non-empty string from the user
# con -----> no
# output --> non-repeated character
# india ---> nda
# indian --> da

def non_repeated_array():
    n = input()
    for i in n:
        if n.count(i) == 1:
            print(i)
            break