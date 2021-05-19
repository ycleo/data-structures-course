#exam2-2-1 Euler Circuit
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Travle1' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER m
#  3. 2D_LONG_INTEGER_ARRAY edges
#

def Travle1(n, m, edges):
    E = [[] for _ in range(n)]
    Deg = [0]*n
    for u, v in edges:
        Deg[u] += 1
        Deg[v] += 1
        E[u].append(v)
        E[v].append(u)
    
    if Deg[0] % 2 == 1:
        return 'no'
    
    stack = [0]
    used = [False] * n
    used[0] = True
    
    cnt = 1
    while stack:
        tmp = stack.pop()
        for x in E[tmp]:
            if Deg[x] % 2 == 1:
                return 'no'
            if not used[x]:
                used[x] = True
                stack.append(x)
                cnt += 1
        
    return 'yes' if cnt == n else 'no'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        res = Travle1(n, m, edges)

        fptr.write(res + '\n')

    fptr.close()