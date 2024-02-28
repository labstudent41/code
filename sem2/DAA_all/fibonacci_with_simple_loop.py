import timeit
def f1(n):
    fterm=0
    sterm=1
    nterm=fterm+sterm
    i=0
    while i<=n:
        print(nterm)
        fterm=sterm
        sterm=nterm
        nterm=fterm+sterm
        i+=1
x=int(input("Enter a number:"))
f1(x)
print("Running time=",timeit.timeit())
