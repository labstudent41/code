import timeit

def selection_sort(x):
    l = len(x)
    for i in range(l):
        small = i
        for j in range(i+1, l):
            if x[j] > x[small]:
                small = j
        if small != i:
            temp = x[i]
            x[i] = x[small]
            x[small] = temp
        print(x)
    return x

# main
prices = [88, 96, 73, 41, 9, 33, 55, 23]
print("Data before sort : ", prices)
result = selection_sort(prices)
print("Data after sort : ", result)

print(timeit.timeit())
