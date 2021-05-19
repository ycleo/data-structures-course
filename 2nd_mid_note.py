#practice-5
def CalculateIndegreesAndOutdegrees(nodes_size, edges):
    # Write your code here
    indeg = [0]*nodes_size
    outdeg = [0]*nodes_size
    for u,v in edges:
        indeg[v] += 1
        outdeg[u] += 1
    return [indeg, outdeg]

#practice-6
#DFS approach
def CheckIfConnected(nodes_size, edges, x, y):
    E = [ [] for _ in range(nodes_size) ]
    used = [False] * nodes_size
    stack = []

    for s, t in edges:
        E[s].append(t)
        E[t].append(s)

    used[x] = True
    stack.append(x)

    while len(stack) > 0 :
        s = stack.pop()
        for e in E[s]:
            if not used[e]:
                used[e] = True
                stack.append(e)
    return "yes" if used[y] else "no"

#BFS approach
from collections import deque
def CheckIfConnected(nodes_size, edges, x, y):
    # Write your code here
    E = [[] for _ in range(nodes_size)]
    used = [False] * nodes_size
    
    for s, t in edges:
        E[s].append(t)
        E[t].append(s)
    
    Q = deque([x])
    used[x] = True
   
    while len(Q) > 0:
        tmp = Q.popleft()
        for i in E[tmp]:
            if not used[i]:
                Q.append(i)
                used[i] = True
    
    return 'yes' if used[y] else 'no'

#practice 7
def inOrder(root): #LDR
    if root:
        inOrder(root.left)
        print(root.info, end=' ')
        inOrder(root.right)
    else:
        return

def preOrder(root): #DLR
    if root:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)
    else:
        return

def postOrder(root): #LRD
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')
    else:
        return

from collections import deque
def levelOrder(root):  #Use BFS -> queue
    
    if root:
        Q = deque([root])
    else:
        return
    
    while len(Q) > 0:
        t = Q.popleft()
        print(t.info, end=' ')
        if t.left:
            Q.append(t.left)
        if t.right:
            Q.append(t.right)

#practice 8
#using stack
def CheckGraph(n, m, edges):
    E = [ [] for _ in range(n) ]
    InDeg = [ 0 for _ in range(n) ]
    st = []

    for s,e in edges:
        E[s].append(e)
        InDeg[e] = InDeg[e] + 1
    for i in range(n):
        if InDeg[i] == 0:
            st.append(i)

    cnt = 0
    while len(st) > 0:
        s = st.pop()
        cnt = cnt + 1;

        for e in E[s]:
            InDeg[e] = InDeg[e] - 1
            if InDeg[e] == 0:
                st.append(e)

    return "yes" if cnt == n else "no"

#using queue
from collections import deque
def CheckGraph(n, m, edges):
    N = deque([])
    indeg = [0] * n
    point_to = [[] for _ in range(n)]
   
    for u, v in edges:
        indeg[v] += 1
        point_to[u].append(v)
       
    for i in range(n):
        if indeg[i] == 0:
            N.append(i)
        

    while N:
        tmp = N.popleft()
        for i in point_to[tmp]:
            indeg[i] -= 1
            if indeg[i] == 0:
                N.append(i)
                
    for x in indeg:     
        if x > 0:
            return 'no'
    return 'yes'

#assignment 2-1
def CA(root_id, assets, C):
    for x in C[root_id]:
        assets[root_id] += CA(x, assets, C)
    return assets[root_id]
        
def CalculateGangAsset(n, root_id, edges, assets):
    #find the children for each node
    C = [[] for _ in range(n)]
    for u, v in edges:
        C[u].append(v)
    
    print(C)
    #Calculate Assets  
    CA(root_id, assets, C)
    
    #find the max
    return max(assets)

#assignment 2-2
from collections import deque
def CalculateCosts(n, m, roads):
    
    # Connection and Cost for Roads
    R = [ [] for _ in range(n) ]
    Cost = [0]*n
    
    # Node Dictionary
    V = {v for v in range(n)}
    
    # initial information summary
    for u, v, c in roads:
        R[u].append(v)
        R[v].append(u)
        Cost[u] += c 
    
    #Create a queue for BFS
    Q = deque([0])
    V.discard(0)
    
    #Answer list
    A = [Cost[0]]
    
    #Start calculation
    while Q:
        tmp = Q.popleft()
        for neb in R[tmp]:
            if neb in V:
                Q.append(neb)
                A[-1] += Cost[neb]
                V.discard(neb)
                      
        if not Q and V:
            x = V.pop()
            Q.append(x)
            A.append(Cost[x])
            V.discard(x)
 
    return sorted(A)


#assignment 2-3
def Cal(v):
    #from v nodes pick two to form an edge
    return int((0.5)*v*(v-1))

def journeyToMoon(n, astronaut):
    
    V = { v for v in range(n)}
    E = [[] for _ in range(n)]
    
    for u, v in astronaut:
        E[u].append(v)
        E[v].append(u)
        
    #Creat stack for DFS
    stack = [0]
    V.discard(0)
    A = [1]
    
    while stack:
        tmp = stack.pop()
        for e in E[tmp]:
            if e in V:
                stack.append(e)
                A[-1] += 1
                V.discard(e)
        
        if not stack:
            A[-1] = Cal(A[-1])
            if V:
                stack.append(V.pop())
                A.append(1)       

    return Cal(n) - sum(A)
