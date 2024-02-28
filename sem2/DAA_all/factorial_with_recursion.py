import timeit
def rfacto(n):
    assert n>=0,"Factorial of a negative number does not exist"
    if n<2:
        return 1
    else:
        return n*rfacto(n-1)
x=int(input("Enter a number:"))
print(rfacto(x))
print("Running time=",timeit.timeit())
