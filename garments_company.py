# GARMENTS COMPANY APPAREL
# The garments company apparel wishes to open outlets at various locations.
# The company shortlisted several plots in these locations and wishes to select
# only plots that are square shaped. Write an algorithm to help Apparel find the
# number of plots that it can select for its outlets.
# input -----> the first line of i/p consists of an integer N, and A1,A2,...AN
# representing areas of outlets.
# output ----> print an integer representing the number of plots that will be
# selected for outlets
import math


def garments_company():
    n =[1,2,3,4,5,14,16]
    for i in n:
        number = math.isqrt(i)
        if number*number == i:
            print(i)

garments_company()