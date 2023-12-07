import timeit
def rgcd(a,b):
    if a==b:
        return a
    elif a<b:
        return rgcd(b,a)
    else:
        return rgcd(b,a-b)
n1=int(input("enter first no."))
n2=int(input("enter the second no."))
print("GCD of",n1,n2,"is",rgcd(n1,n2))
print("running time",timeit.timeit())

