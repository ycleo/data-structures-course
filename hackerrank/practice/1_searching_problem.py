#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Search' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY A
#  2. LONG_INTEGER_ARRAY Q
#

def Search(A, Q):
    output = []
    A.sort()
    for element in Q:
        i = bisect_left(A, element)
        if i != len(A) and A[i] == element:
            output.append('yes')
        else:
            output.append('no')
    return(output)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        Q = list(map(int, input().rstrip().split()))

        R = Search(A, Q)

        fptr.write(' '.join(R))
        fptr.write('\n')

    fptr.close()
