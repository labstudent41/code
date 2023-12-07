import timeit
def f3(n):
    fibtable=[0,1]
    for i in range(2,n+1):
        fibtable.append(fibtable[i-1]+fibtable[i-2])
    return fibtable[n]
x=int(input("Enter a number:"))
print(f3(x))
print("Running time=",timeit.timeit())
