#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'PerformOperationsOnLists' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts 2D_LONG_INTEGER_ARRAY operations as parameter.
#

def PerformOperationsOnLists(operations):
    L = [[], []]
    
    for op, id1, po1, id2, po2 in operations:
        if op == 0:
            L[id1].insert(po1, id2)
        elif op == 1:
            L[id1].pop(po1)
        else:
            tmp = L[id2][po2:]
            L[id1] = L[id1][:po1] + tmp + L[id1][po1:]
            L[id2] = L[id2][:po2]
    return(L[0] + L[1])      
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        operations = []

        for _ in range(m):
            operations.append(list(map(int, input().rstrip().split())))

        concatenated_list = PerformOperationsOnLists(operations)

        fptr.write(' '.join(map(str, concatenated_list)))
        fptr.write('\n')

    fptr.close()
