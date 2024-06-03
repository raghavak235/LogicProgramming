# Longest Word
# Write a function that finds the longest word in a sentence.
# If two or more words are found,return the first longest word.
# Characters such as apostophe, comma, period (and the like) count as part of
# the word
# (e.g. O'Connor is 8 characters long).
# input ------> a string from the user
# con --------> no


# Very brilliant logic
def longest_word():
    # Very brilliant logic
    sen ={len(i):i for i in input().split(' ')}
    print(max(sen), sen.get(max(sen)))



longest_word()