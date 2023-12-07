import timeit
def f2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return f2(n-1)+f2(n-2)
x=int(input("Enter a number:"))
print(f2(x))
print("Running time=",timeit.timeit())
