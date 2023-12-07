import timeit
def rfact(n):
    assert n>=0,"factorial of negative no. does not exists"
    if n<2:
        return 1
    else:
        return n*rfact(n-1)

print("recurrive factorial",rfact(5))
print("running time",timeit.timeit())
