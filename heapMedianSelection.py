''' Heap sort code courtesy of Muhit Kumra of GeeksForGeeks '''
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

'''
Linear-Time Median Selection
SELECT(A,k)
1. Split A into n/5 groups with five elements
2. Let b_i be the median of the i-th group (heap sort for each group)
3. Let B = [b_1, b_2, b_3,..., b_n/5]
4. medianB = SELECT(B, len(B)/2)
5. rearrange A around medianB so that elements that are smaller comes before it and elements that are larger comes after. Elements equal to medianB are next to medianB.
6. Let p be the position of j in rearranged A (pivot)
7. if (k < p) return SELECT (A[1...j-1], k)
   if (k = p) return j
   if (k > p) return SELECT (A[j+1...n], k-j)
'''
def select(A, k):
    if(k > len(A)):
        return 0

    if(len(A) < 10):
        heapSort(A)
        if(len(A) % 2 == 0):
            return A[k-1]
        return A[k]

    # 1. Split A into n/5 groups
    S = []
    i = 0
    while(i + 5 < len(A)-1):
        S.append(A[i:i+5])
        i += 5
    S.append(A[i:])  # Append end of A into S

    medians = []    # List of medians of each i-th group
    # 2-3. Use heap sort on each i-th group and append their median to medians
    for sub in S:
        heapSort(sub)
        medians.append(sub[len(sub)//2])
    heapSort(medians)

    # 4. Median of medians
    j = select(medians, len(medians)//2)

    # 5. Rearrange A
    A1 = []     # Elements smaller than j
    A2 = []     # Elements equal to j
    A3 = []     # Elements larger than j
    for i in A:
        if i < j:
            A1.append(i)
        elif i > j:
            A3.append(i)
        else:
            A2.append(i)
    rearrangedA = A1 + A2 + A3

    # 6. Let p be the position of the pivot
    p = rearrangedA.index(j)
    n = len(A)

    if k == p:
        return j
    elif k < p:
        return select(rearrangedA[0:p], k)
    elif k > p:
        return select(rearrangedA[p+1:n], k-p)

# Main driver code
arr = list(map(int, input('Array > ').rstrip().split()))
k = int(input('Index > '))
ans = select(arr, k)
print('Answer:',ans)
