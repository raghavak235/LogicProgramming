# Print all permutations of a string
# Given a string str; the task is to print all the permutations of str.
# A permutation is an arrangement of all or part of a set of objects, with regard
# to the order of the arrangement.
# For instance, the words "bat" and "tab" represent two distinct permutations
# (or arrangements)
# of a similar three-letter word.
# input ----> string from the user
# con ------> no
# output ---> all permutations of the string

def permutations_string(string, i=0):
    if i == len(string):
        print("".join(string))
    for j in range(i, len(string)):
        words =[c for c in string]
        words[i], words[j] = words[j], words[i]
        permutations_string(words, i+1)

permutations_string('ab')