def merge(left, right):
    left_l = len(left)
    right_l = len(right)
    merged = []
    i, j = 0, 0
    while i < left_l and j < right_l:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < left_l or j < right_l:
        merged.extend(left[i:] or right[j:])
    print('Merged:', merged)
    return merged


def mergesort(array):
    l = len(array)
    if l < 2:
        return array
    mid = l // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left, right)


arr = [12, 74, -1, 99, -34, 0]
a1 = [-1, 12, 74]; a2 = [-34, 0, 99]

print(mergesort(arr))
a = [-3, 0, 2, 4, 6]
b = [1, 2, 3]
print(merge(a, b))
            
##print(merge(a1, a2))
