# ou are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.
# input --------> a number from the user
# constriants --> no
# output -------> number of ways

def climb_stairs_fib(n):
    if n ==0 or n == 1:
        return 1
    else:
        return climb_stairs_fib(n-1) + climb_stairs_fib(n-2)


    pass
  