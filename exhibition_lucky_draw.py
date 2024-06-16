# A person went to an exhibition. A lucky draw is going on, where one should buy a ticket.
# And if they ticket number appear on the screen, that ticket will be considered as jackpot winner.
# he knows the secret of picking up the ticket number, which will be considered for the jackpot.
#
# sort the ticket number in the increasing order.
# Now, the difference between the adjacent digits should not be more than 2.
# If his ticket follows the above condition, then there are more chances to win the jackpot.
#
# Given a ticket number, find whether the ticket is eligible to be part of jackpot or not. Print "Yes/No" based on the result.
#
# Input Format
#
# ticket number
#
# Constraints
#
# no
#
# Output Format
#
# Yes or No
#
# Sample Input 0
#
# 171
# Sample Output 0
#
# No

def tickets():
    s='171'
    sint = int(s)
    a=[]
    for i in s:
        a.append(i)
    a.sort()
    s=[]
    for i in range(len(a)-1):
        s.append(abs(int(a[i])-int(a[i+1])))

    for i in s:
        if i>2:
            print('No')
            break
    print('Yes')

    # or
    L = [int(i) for i in input()]
    L.sort()
    flag = True
    for i in range(len(L) - 1):
        if L[i + 1] - L[i] > 2:
            flag = False
            break
    print("Yes" if flag == True else "No")

tickets()
