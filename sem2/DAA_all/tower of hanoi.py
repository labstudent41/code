import timeit
def tower(n,source,destination,temp):
    if n==1:
        print("move disk from source",source,"to destinatiopn",destination)
        return
    tower(n-1,source,temp,destination)
    print("move disk from source",source,"to destination",destination)
    tower(n-1,temp,destination,source)
n=4
tower(n,'A','B','C')
print("running time",timeit.timeit())
