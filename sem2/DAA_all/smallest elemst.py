import timeit
def smallest(x):
    small=0
    l=len(x)
    for i in range(l):
        if x[i]<small:
            x[i]=small
    return small
marks=[77,35,11,26,99,58]
result=smallest(marks)
print("smallest element is",result) 
print("running time",timeit.timeit())
            
