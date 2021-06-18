#BST OPs
class node:
    def __init__(self, key):
        self.v = key
        self.left = None
        self.right = None
    
def Insert(n: node, key):
    #empty tree
    if n is None:  
        return node(key)
    #non-empty tree
    if key < n.v:
        n.left = Insert(n.left, key)
    elif key > n.v:
        n.right = Insert(n.right, key)
    return n

def Search(n, key):
    if n is None:
        return 0
    if key == n.v:
        return 1
    elif key < n.v:
        return Search(n.left, key)
    else:
        return Search(n.right, key)
    
def Pre(n, key):
    cur = n
    pre = 0
    while cur is not None:
        if key > cur.v:
            pre = cur.v
            cur = cur.right 
        else:
            cur = cur.left
            
    return pre

def Suc(n, key):
    cur = n 
    suc = 0
    while cur is not None:
        if key < cur.v:
            suc = cur.v
            cur = cur.left
        else:
            cur = cur.right
    return suc

def Min(n):
    if n is None:
        return 0
    cur = n
    while cur.left is not None:
        cur = cur.left
    return cur.v

def Max(n):
    if n is None:
        return 0
    cur = n
    while cur.right is not None:
        cur = cur.right
    return cur.v
        

def BinarySearchTreeSimulation(m, queries):
    ans = []
    BST_head = None
    for act, key in queries:
        if act == 1:
            BST_head = Insert(BST_head, key)
        
        elif act == 2:
            ans.append( Search(BST_head, key) )
            
        elif act == 3:
            ans.append( Pre(BST_head, key) )
        
        elif act == 4:
            ans.append( Suc(BST_head, key) )
        
        elif act == 5:
            ans.append( Min(BST_head) )
        
        else:
            ans.append( Max(BST_head) )
            
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input().strip())

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    responses = BinarySearchTreeSimulation(m, queries)

    fptr.write('\n'.join(map(str, responses)))
    fptr.write('\n')

    fptr.close()