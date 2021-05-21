#exam 2-2-3
#Longest path in an undirected tree
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Travle3' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. 2D_LONG_INTEGER_ARRAY edges
#
from collections import deque

def BFS(s, n, adj):
    visited = [False] * n
    dist = [-1 for _ in range(n)]
    
    visited[s] = True
    dist[s] = 0
    
    Q = deque([s])
    while Q:
        t = Q.popleft()
        for i in adj[t]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[t] + 1
                Q.append(i)
                
    MaxDist = 0
    
    for j in range(n):
        if dist[j] > MaxDist:
            MaxDist = dist[j]
            nodeindex = j
    
    return nodeindex, MaxDist
    

            
def Travle3(n, edges):
    #adjacency list
    adj = {i:[] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # 1st BFS to find one end point of longest path
    node, Dis = BFS(0, n, adj)
    # 2nd BFS to find the actual longest path
    node_2, LongDis = BFS(node, n, adj)
    
    return LongDis
 

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

        res = Travle3(n, edges)

        fptr.write(str(res) + '\n')

    fptr.close()
