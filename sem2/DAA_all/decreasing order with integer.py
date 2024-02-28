import timeit
def bubble_sort(n):
    x=len(n)
    for i in range(0,x):
        for j in range(i+1,x):
            if n[i]<n[j]:
                temp=n[j]
                n[j]=n[i]
                n[i]=temp
    return n
a=[22,5,6,98,100]
print("data before sort",a)
result=bubble_sort(a)
print("data after sort",a)
print("result",result)
print("running time",timeit.timeit())

            
