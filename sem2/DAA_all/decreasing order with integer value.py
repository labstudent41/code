import timeit
def bubble_sort(n):
    x=len(n)
    for i in range(x,0):
        for j in range(x,i+j):
    
    
 
            if n[j]>n[i]:
                n[j]=n[i]
                n[i
                n[i]=temp
    return n
city=[34,1,39,5,8,36,100]
print("data before sort",city)
result=bubble_sort(city)
print("data after sort",city)
print("result",result)
print("running time",timeit.timeit)
