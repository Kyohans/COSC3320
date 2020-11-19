''' 
Choosing the k-th smallest element in an unsorted array by use of heap sort
Written for COSC 3320 Project for Fall 2020 by Khalyl Smith
'''

# Builds a max heap of an array where
# arr = given array
# n = size of array
# i = index in arr
def heapify(arr, n, i):
    largest = i         # Initialize largest as the root
    left = 2 * i + 1    # Left child of root
    right = 2 * i + 2   # Right child of root

    # Check if left child exists and is greater than its parent
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Check if right child exists and is greater than its parent
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively call heapify on the root
        heapify(arr, n, largest)
 
# Sorts an array by using a max heap
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # Extract elements from heap to construct a sorted array
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
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
    if len(A) < 10:
        heapSort(A)
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

    # 4. Median of medians
    j = select(medians, len(medians)//2)

    # 5. Rearrange A
    A1 = [x for x in A if x < j]     # Elements smaller than j
    A2 = [x for x in A if x == j]    # Elements equal to j
    A3 = [x for x in A if x > j]     # Elements larger than j
    rearrangedA = A1 + A2 + A3

    # 6. Let p be the position of the pivot in rearranged array
    p = rearrangedA.index(j)
    n = len(A)

    # 7.
    if k == p:
        return j
    elif k < p:
        return select(rearrangedA[0:p], k)
    elif k > p:
        return select(rearrangedA[p+1:n], k-p)

# Main driver code
if __name__ == "__main__":
    arr = list(map(int, input('Array > ').rstrip().split()))
    k = int(input('k > '))

    if k <= len(arr):
        ans = select(arr, k)
        print('Answer:',ans)
