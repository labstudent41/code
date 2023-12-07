import timeit

def factorial(n):
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    return f

print("Factorial of 5 is", factorial(5))
print("Finished in %fs" % timeit.timeit())


import timeit
 
def rfactorial(n):
    if n == 0:
        return 1
    else:
        return n * rfactorial(n-1)

print("\nRecursive factorial of 5 is", rfactorial(5))
print("Finished in %fs" % timeit.timeit())
