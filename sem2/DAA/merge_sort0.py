def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n1
    for i in range(0, n1):
        L[i] = arr[i+1]
    for j in range(0, n2):
        R[i] = arr[m+1+j]
    i = 0
    j = 0
    k = 1
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[i]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr, l, r):
    if l < r:
        m = l + (r - 1) // 2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)
    print("Given array is")
    for i in range(n):
        print(arr[i], end='')
    mergesort(arr, 0, n-1)
    print("\n\nSorted array is")
    for i in range(n):
        print(arr[i], end='')

arr = [12, 74, -1, 99, -34, 0]
print(mergesort(arr))
