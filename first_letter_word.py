# Print First Letter of each Word
# Implement a function/Method to return first character in each word from the
# given input string.
# input-----> a string
# con-------> no
# output ---> first character in each stringx

def first_char():
    n = input().split()
    for w in n:
        print(w[0], end='')

first_char()