# Given a string s, and an integer array indices of the same length
# The string s will be shuffled such that the character at the ith position moves to
# indices[i] in the shuffled string, return shuffled string.
# input ---------> a string and an array
# constraint ----> no
# output --------> a string

def string_shuffle_indices():
    input_str= input()
    input_list=[int(i) for i in input().split()]
    # new_str =''
    # mapping_dict={}
    # for i in range(0, len(input_list)):
    #     mapping_dict[input_list[i]] = input_str[i]
    # print(mapping_dict)
    #
    # for i in range(0, len(input_list)):
    #     new_str += mapping_dict.get(i)
    # print(new_str)

    # Another implementation
    b = [0]*len(input_str)
    print(b)
    for i in range(0, len(input_str)):
        print(input_list[i], input_str[i])
        b[input_list[i]] = input_str[i]

    print(b)
string_shuffle_indices()


