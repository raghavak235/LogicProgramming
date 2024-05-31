# Remove Every vowel from a String
# Create a function that takes a string and returns a new string with all vowels
# removed.
# input -------------> a string
# constraints -------> No
# output ------------> a string

def remove_vowels():
    import re
    print(re.sub("[aeiou]", "", input()))