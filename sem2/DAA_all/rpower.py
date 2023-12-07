import timeit
def rpower(m,n):
    if n==1:
        return m
    else:
        return m*rpower(m,n-1)
print("power is",rpower(2,5
                        ))
print("running time",timeit.timeit())
    
