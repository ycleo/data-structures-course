#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'HeapSortInNondecreasingOrder' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY A as parameter.
#
def HeapSort(A):
    output = []
    hq.heapify(A)
    while len(A) > 0:
        output.append(hq.heappop(A)) 
    return(output)
        
def HeapSortInNondecreasingOrder(A):
    # Write your code here
    buffer = A[:]
    buffer = HeapSort(buffer)
    return(buffer)
#
# Complete the 'HeapSortInNonincreasingOrder' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY A as parameter.
#

def HeapSortInNonincreasingOrder(A):
    # Write your code here
    A = list(map(lambda x: x*-1, A))
    buffer = A[:]
    buffer = list(map(lambda x: x*-1, HeapSort(buffer)))
    return(buffer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        non_decreasingly_sorted_A = HeapSortInNondecreasingOrder(A)

        non_increasingly_sorted_A = HeapSortInNonincreasingOrder(A)

        fptr.write(' '.join(map(str, non_decreasingly_sorted_A)))
        fptr.write('\n')

        fptr.write(' '.join(map(str, non_increasingly_sorted_A)))
        fptr.write('\n')

    fptr.close()