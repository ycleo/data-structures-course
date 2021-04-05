#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'MergeSortInNondecreasingOrder' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY A as parameter.
#
def MergeSort(A, compare):
    if len(A)>1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        MergeSort(left, compare)
        MergeSort(right, compare)
        s = 0
        e = 0
        p = 0
        while s < len(left) and e < len(right):
            if compare(left[s], right[e]):    #key step!!!!!!!
                A[p] = left[s]
                s += 1
            else:
                A[p] = right[e]
                e += 1
            p += 1
        
        while s < len(left):
            A[p] = left[s]
            s += 1
            p += 1
        while e < len(right):
            A[p] = right[e]
            e += 1
            p += 1
        
def MergeSortInNondecreasingOrder(A):
    # Write your code here
    buffer = A[:]
    MergeSort(buffer, lambda a,b: a < b)
    return(buffer)
    
#
# Complete the 'MergeSortInNonincreasingOrder' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts LONG_INTEGER_ARRAY A as parameter.
#

def MergeSortInNonincreasingOrder(A):
    # Write your code here
    buffer = A[:]
    MergeSort(buffer, lambda a,b: a > b)
    return(buffer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        non_decreasingly_sorted_A = MergeSortInNondecreasingOrder(A)

        non_increasingly_sorted_A = MergeSortInNonincreasingOrder(A)

        fptr.write(' '.join(map(str, non_decreasingly_sorted_A)))
        fptr.write('\n')

        fptr.write(' '.join(map(str, non_increasingly_sorted_A)))
        fptr.write('\n')

    fptr.close()