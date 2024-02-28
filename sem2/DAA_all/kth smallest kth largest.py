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
a=[22,5,6,98,100]
result=bubble_sort(a)
print(result)
k=int(input("enter a location"))
print("the ",k,"element is ",result[k-1])
print("running time",timeit.timeit())


            
