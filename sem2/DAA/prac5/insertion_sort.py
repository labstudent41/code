# python implementation of isertion sorqt

import timeit
def insertion_sort(x):
    
    l = len(x)
    if l <= 1:
        return
    
    for i in range(1, l):
        key = x[i]
        j = i - 1
        while j >= 0 and key > x[j]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key
        print(x)
        
    return x

##def insertion_sort2(x):
##    
##    l = len(x)
##    if l <= 1:
##        return
##    
##    for i in range(l):
##        for j in range(i+1, l):
##            print(i, j, x)
##            key = x[i]
##            if x[j] < key:
##                x[i] = x[j]
##                x[j] = key
##        
##    return x

# main
temprature = [27, 16, 11, 24, 30, 49]
#temprature = [int(x) for x in input("Enter numbers : ").split(' ')]

print("Insertion sort")
print("Data before sort : ", temprature)

result = insertion_sort(temprature)
print("Data after sort : ", result)

print(timeit.timeit())
