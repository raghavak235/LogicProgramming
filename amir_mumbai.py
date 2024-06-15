# amir is travelling to mumbai, but this time he is taking flight.
# His brother has already told him about luggage weight limits but forgot it. Now he is taking with him 3 trolly bags.
# As per the current airlines which amir will fly. has below weight limits.
# There can be at max 2 check-in and 1 cabin luggage. Check-in has total limit of L1 and Cabin has limit of L2.
# Now, amir has 3 luggage has weights as W1 and W2 and W3 respectively.
# Now he should be smart enough to make sure that he can travel with all the 3 luggage without paying extra charge.
#
# Find out whether amir can take all of his luggage without any extra charges or not.
# If all good and no extra changes were paid, output "Yes" otherwise "No".
#
# Input Format
#
# integers W1,W2,W3 and L1,L2
#
# Constraints
#
# no
#
# Output Format
#
# Yes or No

def luggage():
    # w1+w2+w3 should be less than L1+L2
    w1=  1;w2= 2
    w3 =  3
    l1= 1
    l2=2
    if w1+w2+w3<=l1+l2:
        print('yes')
