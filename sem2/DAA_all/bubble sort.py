import timeit
def bubble_sort(n):
    x=len(n)
    for i in range(0,x):
        for j in range(i+1,x):
            if n[i]>n[j]:
                temp=n[j]
                n[j]=n[i]
                n[i]=temp
    return n
weight=[44,6,7,3,2,4,55]
print("data before sort",weight)
result=bubble_sort(weight)
print("data after sort",weight)
print("result",result)
print("running time",timeit.timeit())

            
