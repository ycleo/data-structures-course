#exam 2-2-4
#Longest path in DAG
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Travle4' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER m
#  3. 2D_LONG_INTEGER_ARRAY edges
#

from collections import deque
def Travle4(n, m, edges):
    
    #out degree
    OD = [0] * n
    #Parent
    P = [[] for _ in range(n)]
    dp = [0] * n
    Vis = [False] * n
    
    for u, v in edges:
        OD[u] += 1
        P[v].append(u)
    
    #Queue for edges
    Q = deque([])
    for i in range(n):
        if OD[i] == 0:
            Vis[i] = True
            for p in P[i]:
                OD[p] -= 1
                Q.append([p, i])
                dp[p] = max(dp[p], 1 + dp[i])
    #print(Q)
                
    while Q:
        tp, tc = Q.popleft()
        if Vis[tp] == False and OD[tp] == 0:
            Vis[tp] = True
            for x in P[tp]:
                dp[x] = max(dp[x], 1 + dp[tp])
                Q.append([x, tp])
                OD[x] -= 1
                #print(Q)
        
    return max(dp)

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

        res = Travle4(n, m, edges)

        fptr.write(str(res) + '\n')

    fptr.close()