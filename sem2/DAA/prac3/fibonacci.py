import timeit

def fibonacci(n):
    fterm = 0
    sterm = 1
    print(fterm, sterm, end=" ")
    nterm = fterm + sterm
    while nterm <= n:
        print(nterm, end=" ")
        fterm = sterm
        sterm = nterm
        nterm = fterm + sterm

fibonacci(100)
print("\nFinished in %fs\n" % timeit.timeit())


import timeit
 
def rfibonacci(n):
    if n <= 1:
        return 1
    else:
        return rfibonacci(n-2) + rfibonacci(n-1)

print(0, end=" ")
for i in range(11):
    print(rfibonacci(i), end=" ")
print("\nFinished in %fs\n" % timeit.timeit())
