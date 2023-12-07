def largest(x, k=1):
    
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
            
    print(x)
    return x[k-1]


marks = [77, 35, 11, 26, 99, 58]
k = 2
result = largest(marks, k)
print(k, "Largest element is", result)
