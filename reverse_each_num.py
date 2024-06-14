# print reverse of each number in an array
# Implement a program to print reverse of each element in an array
# input -----> size and array elements
# con -------> no
# output ----> print reverse of each element in an array

def reverse_each_ele_array():
    l=['121', '131' ,'123' ,'124', '125']
    output=[]
    for i in l:
        print(i[::-1])
    # for i in l:
    #     for j in range(len(str(i))-1, -1,-1):
    #         # xprint(i[j], end=' ')
    #         output.append(i[j])
    #
    # print(output)

reverse_each_ele_array()