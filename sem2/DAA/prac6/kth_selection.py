def largest(x, k):
    l = len(x)
    if k > l or k < 1:
        return None
    for i in range(k):
        large = i
        for j in range(i+1, l):
            if x[j] > x[large]:
                large = j
        if large != i:
            temp = x[i]
            x[i] = x[large]
            x[large] = temp
    return x[k-1]

def smallest(x, k):
    l = len(x)
    if k > l or k < 1:
        return None
    for i in range(k):
        small = i
        for j in range(i+1, l):
            if x[j] < x[small]:
                small = j
        if small != i:
            temp = x[i]
            x[i] = x[small]
            x[small] = temp
    return x[k-1]

# Main
marks = [77, 35, 11, 26, 99, 58]
k = 3

import timeit
print(k, "Largest element is", largest(marks, k))
print("Finished in %fs" %timeit.timeit())

import timeit
print(k, "Smallest element is", smallest(marks, k))
print("Finished in %fs" %timeit.timeit())
