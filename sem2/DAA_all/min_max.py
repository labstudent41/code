import timeit
def min_max(x):
    l=len(x)
    min=0
    max=0
    for i in range(l):
        if x[i]>max:
            max=x[i]
        if x[i]<min:
            min=x[i]
    print("largest is",max)
    print("smallest is",min)

marks=[88,44,-20,36,99,57]
min_max(marks)
print("running time",timeit.timeit())

