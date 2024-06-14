# Kth SHORTEST PROCESSING QUEUE
# A company wishes to modify the technique by which tasks in the processing
# queue are executed.
# There are N processes with unique ID's from 0 to N-1.
# Each of these tasks has its own execution time.
# The company wishes to implement a new algorithm for processing tasks.
# for this purpose, they have identified a value K by the new algorithm,
# the processor will first process the task that has the Kth shortest execution
# time.
# Write an algorithm to find the Kth shortest execution time.
# input ----> array size, k value and array
# output ---> kth shortest execution time.


def kth_shortest_time():
    n=7
    k=5
    l=[9,-3,8,-6,-7,18,10]
    # we need to sort the array and get the fifth-shortest element.
    l.sort()
    print(l[k-1])
