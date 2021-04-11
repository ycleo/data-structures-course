#practice-0 Array-DS
def reverseArray(a):
    a.reverse()
    return(a)

#------------------------------------------------------------------------
#practice-1 Searching Problem
from bisect import bisect_left 

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

#--------------------------------------------------------------------------
#practice-2 Merge Sort on Integer Sequence
def MergeSort(A, compare):
    # Write your code here
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        MergeSort(left, compare)
        MergeSort(right, compare)
        l = 0
        r = 0
        p = 0
        while(l < len(left) and r < len(right)):
            if compare(left[l], right[r]):
                A[p] = left[l]
                l += 1
            else:
                A[p] = right[r]
                r += 1
            p += 1
        while(l < len(left)):
            A[p] = left[l]
            l += 1
            p += 1
        while(r < len(right)):
            A[p] = right[r]  
            r += 1
            p += 1
def MergeSortInNondecreasingOrder(A):
    de_buffer = A[:]
    MergeSort(de_buffer, lambda a, b : a < b)
    return(de_buffer)

def MergeSortInNonincreasingOrder(A):
    in_buffer = A[:]
    MergeSort(in_buffer, lambda a, b : a > b)
    return(in_buffer)

#------------------------------------------------------------------------
#practice-3 Heap Sort on Sequence
import heapq
def HeapSort(A):
    output = []
    heapq.heapify(A)
    while len(A) > 0:
        output.append(heapq.heappop(A))
    return(output)


def HeapSortInNondecreasingOrder(A):
    # Write your code here
    nd_heap = A[:]
    sorted_nd_heap = HeapSort(nd_heap)
    return(sorted_nd_heap)


def HeapSortInNonincreasingOrder(A):
    # Write your code here
    ni_heap = list(map(lambda x: x*-1, A))
    sorted_ni_heap = list(map(lambda x: x*-1, HeapSort(ni_heap)))
    return(sorted_ni_heap)

#------------------------------------------------------------------------
#practice-4 Two Doubly Linked Lists
def PerformOperationsOnLists(operations):
    L = [[], []]
    
    for op, id1, pos, id2, pos2 in operations:
        if op == 0:
            L[id1].insert(pos, id2)
            pass
        elif op == 1:
            L[id1].pop(pos)
        else:
            # get slice is O(n) in python ...
            P1 = L[id2][pos2:] 

            L[id2] = L[id2][:pos2]
            L[id1] = L[id1][:pos] + P1 + L[id1][pos:]
    return L[0] + L[1]

#------------------------------------------------------------------------
#assignment1-1 Merge two sorted linked lists
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(None)
    head = dummy

    while head1 and head2:
        if head1.data > head2.data:
            head1, head2 = head2, head1
        
        head.next = head1
        head1 = head1.next
        head = head.next
    
    if head1 != None:
        head.next = head1
    else:
        head.next = head2

    
    return dummy.next

#------------------------------------------------------------------------
#assignment1-2 Equal Stacks
def equalStacks(h1, h2, h3):
    # Write your code here
    s1, s2, s3 = map(sum, (h1, h2, h3))
   
    while h1 and h2 and h3:
        if s1 == s2 == s3:
            return s1
        smallest = min(s1, s2, s3)
        while s1 > smallest:
            s1 -= h1.pop(0)
        while s2 > smallest:
            s2 -= h2.pop(0)
        while s3 > smallest:
            s3 -= h3.pop(0)
    return 0

#------------------------------------------------------------------------
#assignment1-3 Maximum Element
def getMax(operations):
    # Write your code here
    res = []
    lar = [0]
    
    for i in range(len(operations)):
        op = list(map(int, operations[i].split()))
        
        if op[0] == 1:
            lar.append(max(lar[-1], op[1]))
        elif op[0] == 2:
            lar.pop(-1)
        else:
            res.append(lar[-1])
    return res

#------------------------------------------------------------------------
#assignment1-4 Jesse and Cookies
from heapq import heappop, heappush, heapify

def cookies(k, A):
    heapify(A)
    op = 0
    while A[0] < k and len(A) > 1:
        heappush(A, heappop(A) + 2 * heappop(A))
        op += 1
    return op if A[0] >= k else -1

#------------------------------------------------------------------------
#assignment1-5 Merge K Sorted Sequences
# alternative 0 ----> heap 
from collections import deque
from heapq import heapify, heappop, heappush
infi = math.inf
def MergeKSortedSequences(s):
    ans = []
    theap = [(infi, -1)]   #heap list with tuples
    
    k = len(s)
    n = len(s[0])

    #initiallize
    for i in range(k):
        s[i] = deque(s[i]) #O(1)  #don't use pop() --> it will cause O(n)
        theap.append( (-s[i].popleft(), i) ) #O(k)
    heapify(theap)  #O(k)
    #create a min heap

    while True:
        val, subl = heappop(theap) #O(lgk)
        if val == infi:
            break
            
        ans.append( -val )
        if s[subl]:
            heappush(theap, (-s[subl].popleft(), subl)) #O(lgk)
 
    return ans

# alternative 1  ----> Merge Sort
def MergeTwoSortedList(ListA, ListB):
    """
    A simple function that merges two sorted lists(increase) into one sorted list(increase)
    ListA and ListB must be a sorted list !!!
    """
    MergeList = []
    i = 0
    j = 0
    while( i < len(ListA) and j < len(ListB)):
        if ListA[i] < ListB[j]:
            MergeList.append(ListA[i])
            i += 1
        else:
            MergeList.append(ListB[j])
            j += 1
            
    if i < len(ListA):
        MergeList.extend(ListA[i:])
        
    if j < len(ListB):
        MergeList.extend(ListB[j:])

    return(MergeList)
            
        
    
def MergeKSortedSequences(sequences, n, k):
    # Write your code here
    output = sequences[0][::-1]
    for seq in sequences[1:]:
        output = MergeTwoSortedList(output, seq[::-1])
    return(output[::-1])


# alternative 2
def MergeKSortedSequences(sequences):
    res = []
    times = sum([len(x) for x in sequences])

    for _ in range(times):
        mn = 10**9
        for seq in sequences:
            if len(seq) > 0 and seq[-1] < mn:
                mn = seq[-1]
        res.append(mn)
        for seq in sequences:
            if len(seq) > 0 and seq[-1] == mn: 
                seq.pop()
                break

    return res[::-1]

#------------------------------------------------------------------------
#assignment1-6 Top K Integer Sequence
from heapq import heapify, heappop, heappush
def TopKIntegerSequence(matrix):
    ans = [] 
    mheap = []

    for row in matrix:
        for x in row:
            heappush(mheap, x)
        ans.append(heappop(mheap))

    return ans