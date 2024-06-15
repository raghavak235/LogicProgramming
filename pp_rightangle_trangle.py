# Right Angle Triangle pattern with fixed alphabet symbol

# A
# B B
# C C C
# D D D D
def fixed_alphabet():
    n=4
    #A ord 65
    for i in range(n):
        print((chr(65+i)+' ')*(i+1))


fixed_alphabet()