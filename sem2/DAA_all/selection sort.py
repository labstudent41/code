import timeit
def sel(n):
    x=len(n)
    for i in range(0,x):
        small=i
        for j in range(i+1,x):
            if n[j]<n[small]:
                small=j
                print(c)
                
        if small!=i:
            temp=n[i]
            n[i]=n[small]
            n[small]=temp
            print(c)

c=[27,16,11,24,30,49]
print("data before sort",c)
result=sel(c)
print("data after sort",result)
print("time",timeit.timeit())
