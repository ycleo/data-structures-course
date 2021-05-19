#exam 2-2-2  Hamiltonian circuit 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Travle2' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER m
#  3. 2D_LONG_INTEGER_ARRAY edges
#
HC = 'no'

def BT(n, V, M, arr, x):
    a = arr[x-1]
    if(x == n):     
        if M[a][arr[0]] == 1: #find one solution
            return 'yes'
        
    for b in range(n):
        if M[a][b] == 1 and not V[b]:
            V[b] = True
            arr[x] = b
            re = BT(n, V, M, arr, x+1)
            if re == 'yes':
                return 'yes'
            V[b] = False
    
    return 'no'

            
def Travle2(n, m, edges):
    #array for backtracking
    arr = [-1]*n
    
    #visited or not
    V = [False]*n
    
    #adjacency matrix
    M = [[0]*n for _ in range(n) ]
    for u, v in edges:
        M[u][v] = 1
        M[v][u] = 1
        
    V[0] = True
    arr[0] = 0
    
    #Back Tracking
    return BT(n, V, M, arr, 1)
    
    
    

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

        res = Travle2(n, m, edges)

        fptr.write(res + '\n')

    fptr.close()