# Even Length Words
# Write a program to print even length words in a string?
# input -----> a string from the user
# con -------> no
# output ----> list of strings with even length

def even_len_words():
    sen =input().split()
    for w in sen:
        if w%2 == 0:
            print(w)
