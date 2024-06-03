# Removing Duplicate Characters from a string
# Given a string S, the task is to remove all the duplicates in the given string.
# input --------> a string from the user
# con ----------> remove all dup
# output -------> a string without duplicates

def remove_duplicates():
    no_dup=set((input()))
    # """Remove duplicate characters from a string using a set."""
    #  You can use join to set values to construct the string
    str_nodup =  ''.join(no_dup)
    print(str_nodup)
remove_duplicates()
