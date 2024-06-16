# There are 3 friends named Ronaldo,Messi,Rooney who worked at a company.
# Given their monthly salaries and monthly expenditures, returns the highest saving among them.
#
# Input Format
#
# single line with 6 space seperated integers.
#
# Constraints
#
# no
#
# Output Format
#
# the highest saving among the 3 of them
#
# Sample Input 0
#
# 10 7 15 10 15 11
# Sample Output 0
#
# 5

def company_salary():
    a1,a2,b1,b2,c1, c2 =(int(i) for i in input().split())
    print(
        max(a1-a2,b1-b2,c1-c2)
    )

