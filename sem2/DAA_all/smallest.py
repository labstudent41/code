import timeit
def smallest(x):
    small=x[0]
    l=len(x)
    for i in range(1,l): 
        if x[i]<small:
            small=x[i]
    return small
marks=[77,35,11,26,99,58]
result=smallest(marks)
print("smallest element is",result) 
print("running time",timeit.timeit())
            
