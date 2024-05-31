# Jewels and Stones
# You are given Strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a type
# of stone you have you want to know how many of the stones you have are also
# jewels.
# Letter are case-sensitive. so "a" is considered as a different type of stone from
# "A".
# input ------> A string
# constriant -> no
# output -----> how many of the stones

def jewels_and_stones():
    jewels = input()
    stones = input()
    jewels_count =0
    for j in jewels:
        if j in stones:
            jewels_count+=stones.count(j)

    print(jewels_count)


jewels_and_stones()



