# In an online exam, the test paper set is categorized by the letters A-Z. The students enrolled in the exam have been assigned a numeric value called application ID. To assign the test set to the student, firstly the sum of all digits in the application ID is calculated. If the sum is within the numeric range 1-26 the corresponding alphanetic set code is assigned to the student, else the sum of the digits are calcualted again and so on unitil the sum falls within the 1-26 range.
#
# Input Format
#
# application id as int
#
# Constraints
#
# no
#
# Output Format
#
# set number
#
# Sample Input 0
#
# 123
# Sample Output 0
#
# F

def sum(n):
    sum=0
    while n!=0:
        d=n%10
        sum=sum+d
        n=n//10
    return sum

n=int(input())
while True:
    if n>=1 and n<=26:
        print(chr(n+64))
        break
    else:
        n=sum(n)