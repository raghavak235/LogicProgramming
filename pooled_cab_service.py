# POOLED CAB SERVICE
# A compnay wishes to provide cab service for their N employees.
# The employees have distance ranging from 0 to N-1.
# The company has calculated the total distance from an employee's residence
# to the company,
# considering the path to be followed by the cab is a straight path.
# The distance of the company from it self is 0.
# The distance for the employees who live to the left side of the company is
# represented with a negative sign.
# The distance for the employees who live to the right side of the company is
# represented with a positive sign.
# the cab will be allotted a range of distance.
# The company wishes to find the distance for the employees who live within the
# particular distance range.
# write a alogrithm to find the distance for the employees who live within the
# distance range.
# input ----> size of the list N ,SD,ED and an array of distance
# output ---> distance within the range else -1
# con ------> con

def cab_service():
    lb=30
    up=50
    l=[29,38,12,48,39,55]
    # we need to verify whether the array distance is between lb,up
    for i in l:
        if lb<=abs(i)<=up:
            print(i)

cab_service()