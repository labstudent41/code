import timeit
def largest(x):
    large=0
    l=len(x)
    for i in range(l):
        if x[i]>large:
            large=x[i]
    return large
marks=[77,35,11,26,99,58]
result=largest(marks)
print("largest element is",result) 
print("running time",timeit.timeit())
            
