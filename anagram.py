# Anagrams
# Two strings a and b are called anagrams, if they contain all the same characters
# in the same frequencies.
# input --------> two strings a and b
# constraint ---> no
# output -------> true or false



# char_count1 == char_count2
    #  when you use the == operator to compare two dictionaries in Python, both the keys and their  corresponding values
    # are verified.The dictionarie are considered equal if and only if they
    # have the exact same set of keys and the values for each key are the same in both dictionaries.

def anagram_strings():
    a = input()
    b = input()
    a_comp_dict={}
    b_comp_dict={}
    for i in a:
        if i not in a_comp_dict:
                a_comp_dict[i] = 1
        else:
            a_comp_dict[i] += 1

    for i in b:
        if i not in b_comp_dict:
                b_comp_dict[i] = 1
        else:
            b_comp_dict[i] += 1

    # char_count1 == char_count2
    #  when you use the == operator to compare two dictionaries in Python, both the keys and their  corresponding values
    # are verified.The dictionarie are considered equal if and only if they
    # have the exact same set of keys and the values for each key are the same in both dictionaries.

    print(a_comp_dict==b_comp_dict)



anagram_strings()