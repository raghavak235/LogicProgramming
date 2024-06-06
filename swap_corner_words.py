# Swap corner words and reverse middle characters,
# Write a Java program to take an input string and exchange the first and last
# word and reverse the middle word.
# input -------> a string
# con ---------> no
# output ------> a string

def corner_words_rev():
    inp = input().split()
    print(inp[-1], end=' ')
    for i in range(len(inp)-2, 0, -1):
        print(inp[i][::-1], end=' ')

    print(inp[0])
corner_words_rev()